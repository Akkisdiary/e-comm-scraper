"""Extract search results for a term on amazon.com"""

import sys

from furl import furl
from lxml import html

import web
from utils import xpath


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
            link = xpath.extract(item, ".//div[@data-cy='title-recipe']//a", 0)
            if link:
                url = xpath.extract(link, ".//a/@href", 0)
                title = xpath.extract(link, ".//text()")

                results.append({
                    "url": url,
                    "title": "".join(title),
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
    headers = web.random_headers()

    return web.get(url.url, headers=headers)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError("Please enter a search term")
    
    search_term = sys.argv[1]
    print(f"Searching for '{search_term}'...")

    response = get_search_response(search_term)
    validate_response(response)

    results = extract_search_results(response.text)

    print(results)