"""Utility functions to extract data using xpath rules"""

from typing import List, Optional, Union, Type

from lxml.html import HtmlElement


def extract(
    element: Type[HtmlElement],
    xpath: Union[str, List[str]], 
    index: Optional[int] = None
):
    if not isinstance(xpath, (list, tuple)):
        xpath = [xpath]
    
    results = []

    for path in xpath:
        results.extend(element.xpath(path))

    if isinstance(index, int):
        try:
            return results[index]
        except IndexError as e:
            return None
    
    return results