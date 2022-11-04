import json
from pathlib import Path
from typing import Optional
from urllib.parse import quote_plus

import pandas as pd
import requests
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
from retry.api import retry_call

API_KEY = "YOUR SCRAPING FISH API KEY"  # https://scrapingfish.com/buy
url_prefix = f"https://scraping.narf.ai/api/v1/?api_key={API_KEY}&url="
concurrency = 10


def request_html(url: str) -> Optional[str]:
    response = requests.get(url, timeout=90)
    if response.ok:
        return response.content
    if response.status_code == 404:
        return None
    response.raise_for_status()


df = pd.read_csv("product_urls.csv")
Path("./products/").mkdir(parents=True, exist_ok=True)


def scrape_product(url: str):
    product_id = url.split("/")[-1]
    if not product_id.isdigit():
        print(f"Invalid product id {product_id}")
        return
    html = retry_call(request_html, fargs=[f"{url_prefix}{quote_plus(url)}"], tries=10)
    if html is None:
        print(f"404 for url {url}")
        return
    soup = BeautifulSoup(html, "html.parser")
    json_element = soup.find("script", {"id": "__NEXT_DATA__"})
    if json_element is None:
        print(f"No json data for url {url}")
        return
    try:
        page_json = json.loads(json_element.text)
    except Exception as e:
        print(f"Error for url {url}")
        print(e)
        return
    data = page_json.get("props", {}).get("pageProps", {}).get("initialData", {}).get("data", {})
    product_json = {"data": {k: data.get(k) for k in ["product", "idml", "reviews"]}}
    product_id = url.split("/")[-1]
    with open(f"./products/{product_id}.json", "w") as f:
        json.dump(product_json, f)


Parallel(n_jobs=concurrency, verbose=1)(delayed(scrape_product)(url) for url in df["product_url"].unique())
