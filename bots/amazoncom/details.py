"""Extract details from amazon.com products from a given csv file"""

import re
import sys
from datetime import datetime
from typing import Dict, List, Type, Any

import pandas as pd
from furl import furl
from lxml import html
from lxml.html import HtmlElement

import web
from utils import export, xpath
from bots.amazoncom import constants


def read_urls_from_csv(filepath: str):
    df = pd.read_csv(filepath)
    if "url" not in df.columns:
        raise ValueError("The given csv file does not contain urls")

    return df["url"].to_list()


def get_asin(doc: Type[HtmlElement], url: str):
    def _run_asin_regexes(value):
        for regex in constants.ASIN_REGEXES:
            asin = re.findall(regex, value)
            if asin:
                return asin[0]

    asin = None

    if doc is not None:
        asin = xpath.extract(doc, constants.ASIN_PATHS, 0)
        if doc.xpath('//script[contains(. ,\'"parentAsin":"{0}\')]'.format(asin)):
            # don't allow the parent asin to be the asin
            asin = None

    if not asin and url:
        asin = _run_asin_regexes(url)

    if asin and any(u in asin for u in ("/gp/", "/dp/")):
        asin = _run_asin_regexes(asin)

    if not asin:
        return None

    return asin.split(".")[-1].strip()


def validate_response(response: web.Response):
    response.raise_for_status()


def get_product_response(url: str):
    url = furl(url)
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    headers = web.random_headers(**headers)

    return web.get(url.url, headers=headers)


def extract_product_details(html_content: str, url: str):
    result = {}
    doc = html.fromstring(html_content)

    result["title"] = xpath.extract(doc, constants.TITLE_PATHS, 0)
    result["brand"] = xpath.extract(doc, constants.BRAND_PATHS, 0)
    result["price"] = xpath.extract(doc, constants.PRICE_PATHS, 0)
    result["list_price"] = xpath.extract(doc, constants.REGULAR_PRICE_PATHS, 0)
    result["image"] = xpath.extract(doc, constants.IMAGE_PATHS, 0)
    result["sku"] = get_asin(doc, url)

    return result


def extract(urls: List[str]):
    data = []
    
    for url in urls:
        response = get_product_response(url)
        validate_response(response)

        details = extract_product_details(response.content, url)
        data.append(details)

    return data


def clean_and_transform(raw_data: List[Dict[str, Any]]):
    schema = {
        "title": [],
        "brand": [],
        "price": [],
        "list_price": [],
        "image": [],
        "sku": [],
    }
    for data in raw_data:
        for key in schema.keys():
            val = data.get(key)
            if val is not None:
                val=  str(val).strip()
            schema[key].append(val)

    return schema


def main(urls: List[str]):
    print(f"Reading csv: {filepath}")
    urls = read_urls_from_csv(filepath)

    print(f"Extrating product information ({len(urls)} urls)")
    raw = extract(urls)
    final = clean_and_transform(raw)

    file_name = f"amazoncom-details-{datetime.now().isoformat(timespec='seconds')}"
    export.to_csv(final, file_name)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError("Please enter a csv file path")
    
    filepath = sys.argv[1]
    main(filepath)
    
    print("===COMPLETE===")