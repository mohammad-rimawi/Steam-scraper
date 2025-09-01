from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import time
import csv

url = "https://store.steampowered.com/specials"
target_games = int(input("how much game you want? "))

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        games_loaded = 0
        click_limit = 20
        all_games = []

        for _ in range(click_limit):
            page.wait_for_timeout(2000)
            html = page.content()  
            tree = HTMLParser(html)
            divs = tree.css('div[class="ImpressionTrackedElement"]')
            games_loaded = len(divs)

            if games_loaded >= target_games and _ > 0:
                break

            try:
                page.click('button[class*="btnv6_lightblue"]')
            except:
                break

        html = page.content()
        browser.close()
        tree = HTMLParser(html)
        divs = tree.css('div[class="ImpressionTrackedElement"]')[:target_games]

        for d in divs:
            title_elem = d.css_first('div[class *= "StoreSaleWidgetTitle"]')
            img_elem = d.css_first('img[class="_2eQ4mkpf4IzUp1e9NnM2Wr"]')
            tag_elem = d.css('div[class="_2bkP-3b7dvr0a_qPdZEfHY"] > a')

            if not title_elem:
                continue

            title_tag = title_elem.text()
            thumbnail = img_elem.attributes.get("src") if img_elem else ""
            tags = [a.text() for a in tag_elem[:5]] if tag_elem else []

            attrs = {
                "title": title_tag,
                "game tags": ", ".join(tags),
                "thumbnail": thumbnail
            }

            all_games.append(attrs)

        print(len(all_games))

        with open("steam_games.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["title", "game tags", "thumbnail"])
            writer.writeheader()
            writer.writerows(all_games)