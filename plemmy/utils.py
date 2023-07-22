import logging
import requests


def post_handler(url: str, headers: dict, json: dict) -> requests.Response:
    """ post_handler: handles all POST operations for Plemmy

    Args:
        url (str): Lemmy API URL
        headers (dict): optional headers
        json (dict): json/form data to be posted

    Returns:
        requests.Response: server response for POST operation
    """

    logger = logging.getLogger(__name__)
    try:
        re = requests.post(url, headers=headers, json=json, timeout=30)
        logger.debug(f"Code: {re.status_code}")
    except requests.exceptions.RequestException as ex:
        logger.error(f"POST error: {ex}\n\nURL: {url}" +
                     f"\nheaders: {headers}\njson: {json}")
        return None
    return re


def put_handler(url: str, headers: dict, json: dict) -> requests.Response:
    """ put_handler: handles all PUT operations for Plemmy

    Args:
        url (str): Lemmy API URL
        headers (dict): optional headers
        json (dict): json/form data being supplied

    Returns:
        requests.Response: server response for PUT operation
    """

    logger = logging.getLogger(__name__)
    try:
        re = requests.put(url, headers=headers, json=json, timeout=30)
        logger.debug(f"Code: {re.status_code}")
    except requests.exceptions.RequestException as ex:
        logger.error(f"PUT error: {ex}\n\nURL: {url}" +
                     f"\nheaders: {headers}\njson: {json}")
        return None
    return re


def get_handler(url: str, headers: dict, json: dict,
                params: dict = None) -> requests.Response:
    """ get_handler: handles all GET operations for Plemmy

    Args:
        url (str): Lemmy API URL
        headers (dict): optional headers
        json (dict): json/form data
        params (dict): parameters for GET operation

    Returns:
        requests.Response: server response for GET operation
    """

    logger = logging.getLogger(__name__)
    try:
        re = requests.get(url, headers=headers, json=json, params=params,
                          timeout=30)
        logger.debug(f"Code: {re.status_code}")
    except requests.exceptions.RequestException as ex:
        logger.error(f"GET error: {ex}\n\nURL: {url}" +
                     f"\nheaders: {headers}\njson: {json}")
        return None
    return re


def create_form(arguments: dict) -> dict:
    """ create_form: creates a dictionary out of supplied arguments (derived
    from locals()); resulting dict is in form {"arg1", arg1, ... "argN", argN}

    Args:
        arguments (dict): function arguments supplied with locals()

    Returns:
        dict: constructed dictionary/form
    """
    return {k: str(v).lower() if isinstance(v, bool) else v for k, v in arguments.items()
            if v is not None and k != "self"}
