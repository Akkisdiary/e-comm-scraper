"""Utility functions to extract data using xpath rules"""

from typing import List, Union
from lxml.etree import Element


def extract(
    element: Element,
    xpath: Union[str, List[str]], 
    index: int = 0
):
    if not isinstance(xpath, (list, tuple)):
        xpath = [xpath]
    
    results = []

    for path in xpath:
        results.extend(element.xpath(path))

    if index:
        try:
            return results[index]
        except IndexError as e:
            return None
    
    return results