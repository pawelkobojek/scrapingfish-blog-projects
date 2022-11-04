# Scraping Walmart by Scraping Fish 🐟

The code for data gathering and exploration for blog post [Scraping Walmart to estimate share of sugar in food](https://scrapingfish.com/blog/scraping-walmart).

This folder contains scripts for scraping publicly available Walmart product details data using [Scraping Fish API](https://scrapingfish.com).
Data exploration code is in the `walmart-data-exploration` python notebook.
To be able to run web scraping scripts and actually scrape the data, you will need Scraping Fish API key which you can get here: [Scraping Fish Request Packs](https://scrapingfish.com/buy).
A starter pack of 1,000 API requests costs only $2 and will let you play with the API on your own ⛹️.
Without Scraping Fish API key you are likely to see captcha instead of useful product detail information ⛔️.

Scraping Fish is a premium API for scraping powered by rotating 4G/LTE proxy by default.
It is the best available proxy type for scraping since mobile IPs are ephemeral and constantly reassigned between real users.
This type of proxy is capable of scraping even the most demanding websites without being blocked.
You can read more on advanced topics in Scraping Fish API [Documentation](https://scrapingfish.com/docs/intro).

## Prerequisites

- python 3.10
- `pip install -r requirements.txt`

## Web scraping scripts

### Category URLs

`prepare_category_urls.py` is a script which selects categories from Walmart site map XML file which you can find here: https://www.walmart.com/sitemap_browse_fst.xml.

Download `sitemap_browse_fst.xml` file and adjust `selected_category` variable according to your needs.

After executing the script (`python prepare_category_urls.py`), you should see `category_urls.txt` file which will be used in the next step.

### Product URLs

`scrape_product_urls.py` iterates category URLs in `category_urls.txt` file and scrapes product identifiers.
It also handles pagination.

Remember to set `API_KEY` variable to your Scraping Fish API key.

After executing the script (`python scrape_product_urls.py`), you should see `product_urls.csv` file containing product URLs which will be used in the next step.

### Product details

`scrape_product_details.py` iterates product URLs from `product_url` column to scrape product HTML and extracts a JSON with product details.
The result is saved into `{product_id}.json` file in `./products` folder.

Remember to set `API_KEY` variable to your Scraping Fish API key.

After executing the script (`python scrape_product_details.py`), you should see `./products` folder containing JSON files with product details named by product identifier.

## Data exploration

To run nutrition facts data exploration for food category products based on scraped data run jupyter server:

```
jupyter notebook
```

and open `walmart-data-exploration.ipynb` notebook.
