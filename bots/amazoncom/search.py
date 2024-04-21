"""Extract search results for a term on amazon.com"""

import sys

from datetime import datetime
from typing import Dict, List

from furl import furl
from lxml import html

import web
from utils import xpath, export


SEARCH_URL = "https://www.amazon.com/s/ref=nb_sb_noss_2"


def validate_response(response):
    response.raise_for_status()


def extract_search_results(html_content: str):
    """Extract the search resutls from supplied html content

    Args:
        html_content (str): The html document

    Returns:
        List[Dict[str, str]]: List of results in json format
    """
    results = []
    doc = html.fromstring(html_content)

    items = xpath.extract(doc, "//div[@data-csa-c-type='item']")
    if len(items) > 0:
        for item in items:
            link = xpath.extract(item, ".//div[@data-cy='title-recipe']//h2/a", 0)
            if link is not None:
                results.append({
                    "url": xpath.extract(link, "./@href", 0),
                    "title": "".join(xpath.extract(link, ".//text()")),
                    "price": "".join(xpath.extract(item, ".//span[@class='a-price']//span[@class='a-offscreen']//text()")),
                    "list_price": "".join(xpath.extract(item, ".//span[@data-a-strike='true']//span[@class='a-offscreen']//text()")),
                })

    return results


def get_search_response(search_term: str):
    """Get the http response for the search term

    Args:
        search_term (str): The term to search for

    Returns:
        requests.Response: The http response
    """
    url = furl(SEARCH_URL)
    url.args.update({
        "url": "search-alias=aps",
        "field-keywords": search_term,
        "sprefix": f"{search_term},aps,399",
        "k": search_term,
    })
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


def clean_and_transform(data: List[Dict[str, str]]):
    df = {
        "title": [],
        "price": [],
        "list_price": [],
        "url": [],
    }

    for r in data:
        url = r.get("url")
        title = r.get("title")
        price = r.get("price")
        list_price = r.get("list_price")

        if all((url, title)):
            if not url.startswith("http"):
                url = f"https://www.amazon.com{url}"

            df["title"].append(title)
            df["url"].append(url)
            df["price"].append(price)
            df["list_price"].append(list_price)

    return df


def extract(search_term: str):
    response = get_search_response(search_term)
    validate_response(response)

    raw = extract_search_results(response.text)
    return raw


def main(search_term: str):
    print(f"Searching for '{search_term}'...")
    raw = extract(search_term)

    print("Transforming & cleaning the data...")
    final = clean_and_transform(raw)

    file_name = f"amazoncom-search-{search_term}-{datetime.now().isoformat(timespec='seconds')}"
    export.to_csv(final, file_name)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError("Please enter a search term")
    
    search_term = sys.argv[1]
    main(search_term)
    print("===COMPLETE===")