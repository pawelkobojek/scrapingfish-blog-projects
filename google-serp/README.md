# Google SERP by Scraping Fish 🐟

Google SERP scraping code for blog post [Scraping Google SERP with Geolocation](https://scrapingfish.com/blog/google-serp-geolocation).

This folder contains a script for scraping Google SERP with geolocation using [Scraping Fish API](https://scrapingfish.com).
To be able to run the script, you will need Scraping Fish API key which you can get here: [Scraping Fish Request Packs](https://scrapingfish.com/buy).
A starter pack of 1,000 API requests costs only $2 and will let you play with the API on your own ⛹️.
Without Scraping Fish API you are likely to see captcha ⛔️ instead of relevant Google SERP.

Scraping Fish is a premium API for web scraping powered by [ethically-sourced](https://scrapingfish.com/how-ips-for-web-scraping-are-sourced) rotating 4G/LTE mobile proxy.
You can read more on advanced topics in Scraping Fish API [Documentation](https://scrapingfish.com/docs/intro).

## Prerequisites

- python 3.10
- `pip install -r requirements.txt`

## Usage

Usage:

```
google_serp.py [-h] --api-key API_KEY --keyword KEYWORD [--country COUNTRY] --location LOCATION
    [--language LANGUAGE] [--output OUTPUT]

Google SERP using Scraping Fish API.

options:
  -h, --help           show this help message and exit
  --api-key API_KEY    Scraping Fish API key: https://scrapingfish.com/buy
  --keyword KEYWORD    Keyword to search
  --country COUNTRY    Country code for `gl` parameter (default: us)
  --location LOCATION  Location canonical name for `uule` parameter
  --language LANGUAGE  Language code for `hl` parameter (default: en)
  --output OUTPUT      Output file path (default: ./google.html)
```

Examples:

```
python google_serp.py --api-key "YOUR_SCRAPING_FISH_API_KEY" \
    --keyword "coffee shop" \
    --location "California,United States"
```

```
python google_serp.py --api-key "YOUR_SCRAPING_FISH_API_KEY" \
    --keyword "coffee shop" \
    --country "cz" \
    --location "Old Town,Prague,Czechia" \
    --language "cs" \
    --output "coffee-shop-cz.html"
```

Remember to set `--ap-key` to your Scraping Fish API key: https://scrapingfish.com/buy.

After executing the script, you should see the website saved in specified output file, `./google.html` by default.
