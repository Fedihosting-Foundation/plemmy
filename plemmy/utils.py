import logging
import requests


def post_handler(url: str, headers: dict, json: dict) -> requests.Response:

    logger = logging.getLogger(__name__)
    try:
        re = requests.post(url, headers=headers, json=json)
        logger.debug(f"Code: {re.status_code}")
    except requests.exceptions.RequestException as ex:
        logger.error(f"POST error: {ex}\n\nURL: {url}" +
                     f"\nheaders: {headers}\njson: {json}")
        return None
    return re


def put_handler(url: str, headers: dict, json: dict) -> requests.Response:

    logger = logging.getLogger(__name__)
    try:
        re = requests.put(url, headers=headers, json=json)
        logger.debug(f"Code: {re.status_code}")
    except requests.exceptions.RequestException as ex:
        logger.error(f"PUT error: {ex}\n\nURL: {url}" +
                     f"\nheaders: {headers}\njson: {json}")
        return None
    return re


def get_handler(url: str, headers: dict, json: dict, params: dict = None) -> requests.Response:

    logger = logging.getLogger(__name__)
    try:
        re = requests.get(url, headers=headers, json=json, params=params)
        logger.debug(f"Code: {re.status_code}")
    except requests.exceptions.RequestException as ex:
        logger.error(f"GET error: {ex}\n\nURL: {url}" +
                     f"\nheaders: {headers}\njson: {json}")
        return None
    return re


def create_form(arguments: dict) -> dict:

    return {k: v for k, v in arguments.items()
            if v is not None and k != "self"}
