"""Wrapper around `requests` library for centralized control"""
from typing import Any, Dict, List, Type

from requests import Response
import requests as r


def request(
    method: str,
    url: str,
    *args: List[Any],
    max_retries: int = 0,
    **kwargs: Dict[str, Any],
) -> Type[Response]:
    attempt = 0
    while attempt <= max_retries:
        attempt += 1
        response = r.request(method, url, *args, **kwargs)

    return response


def get(url, *args, **kwargs):
    return request("GET", url, *args, **kwargs)


def post(url, *args, **kwargs):
    return request("POST", url, *args, **kwargs)