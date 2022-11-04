from typing import Optional
from urllib.parse import quote_plus

import pandas as pd
import requests
from bs4 import BeautifulSoup
from retry.api import retry_call
from tqdm import tqdm

API_KEY = "YOUR SCRAPING FISH API KEY"  # https://scrapingfish.com/buy
url_prefix = f"https://scraping.narf.ai/api/v1/?api_key={API_KEY}&url="


def request_html(url: str) -> Optional[str]:
    response = requests.get(url, timeout=90)
    if response.ok:
        return response.content
    if response.status_code == 404:
        return None
    response.raise_for_status()


with open("category_urls.txt", "r") as f:
    category_urls = f.read().splitlines()

try:
    df = pd.read_csv("product_urls.csv")
except:
    df = pd.DataFrame({"category_code": [], "category_name": [], "product_url": []})
    df.to_csv("product_urls.csv", index=False, mode="a")

with tqdm() as pbar:
    for url in category_urls:
        category_products = set()
        category = ""
        page = 0
        while page < 100:
            page = page + 1
            browse_url = (
                quote_plus(url + f"?page={page}&affinityOverride=default") if page > 1 else quote_plus(url + "/")
            )
            category_html = retry_call(request_html, fargs=[f"{url_prefix}{browse_url}"], tries=10)
            if category_html is None:
                print(f"\n404 for url {browse_url}")
                break
            soup = BeautifulSoup(category_html, "html.parser")
            results_container = soup.find("div", {"id": "results-container"})
            if results_container:
                if page == 1:
                    category = results_container.find("h1").text
                    print(f"\n{category}")
                page_products = set(
                    [
                        href.get("link-identifier")
                        for href in results_container.parent.find_all("a", {"link-identifier": True})
                    ]
                )
                category_products = category_products.union(page_products)
            pbar.update()
            if len(soup.find_all("a", {"aria-label": "Next Page"})) == 0:
                break
        category_product_urls = [f"https://www.walmart.com/ip/{p}" for p in category_products]
        df = pd.DataFrame(
            {
                "category_code": [url.split("/")[-1]] * len(category_products),
                "category_name": [category] * len(category_products),
                "product_url": category_product_urls,
            }
        )
        df.to_csv("product_urls.csv", index=False, header=False, mode="a")
