# Steam Games Scraper

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Playwright](https://img.shields.io/badge/Playwright-Installed-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Steam Games Scraper** is a Python tool that uses [Playwright](https://playwright.dev/python/docs/intro) and [Selectolax](https://github.com/rushter/selectolax) to scrape discounted games from the Steam store.

---

## Features

- Scrape discounted Steam games from the Specials page.
- Extract the following information:
  - Game title
  - Tags
  - Thumbnail image URL
- Export scraped data to CSV (`steam_games.csv`).
- Supports scraping a custom number of games.
- Handles dynamic page loading with Playwright.

---

## Requirements

- Python 3.9 or higher
- Required Python packages:
```bash
pip install playwright selectolax
playwright install
