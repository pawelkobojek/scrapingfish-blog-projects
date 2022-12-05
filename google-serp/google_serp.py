import argparse
from urllib.parse import quote_plus

import requests
import uule_grabber


def parse_args():
    example_usage = """
    example: python google_serp.py 
        --api_key "YOUR_SCRAPING_FISH_API_KEY" 
        --keyword "coffee shop" 
        --location "California,United States"
    """
    parser = argparse.ArgumentParser(description="Google SERP using Scraping Fish API.", epilog=example_usage)
    parser.add_argument(
        "--api-key",
        help="Scraping Fish API key: https://scrapingfish.com/buy",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--keyword",
        help="Keyword to search",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--country",
        help="Country code for `gl` parameter (default: us)",
        required=False,
        type=str,
        default="us",
    )
    parser.add_argument(
        "--location",
        help="Location canonical name for `uule` parameter",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--language",
        help="Language code for `hl` parameter (default: en)",
        required=False,
        type=str,
        default="en",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: ./google.html)",
        required=False,
        type=str,
        default="./google.html",
    )
    return parser.parse_args()


def main(api_key, keyword, location, country, language, output):
    keyword = quote_plus(keyword)
    uule = uule_grabber.uule(location)
    country_code = country
    language_code = language
    search_url = f"https://www.google.com/search?q={keyword}&uule={uule}&gl={country_code}&hl={language_code}"
    url_prefix = f"https://scraping.narf.ai/api/v1/?api_key={api_key}&url="
    response = requests.get(f"{url_prefix}{quote_plus(search_url)}", timeout=90)
    with open(output, "wb") as f:
        f.write(response.content)
        print(f"Result saved to {output}")


if __name__ == "__main__":
    args = parse_args()
    main(
        api_key=args.api_key,
        keyword=args.keyword,
        location=args.location,
        country=args.country,
        language=args.language,
        output=args.output,
    )
