import logging
import requests


def create_session(headers: dict, jwt: str) -> requests.Session:
    """ create_session: create a `requests.Session` session given supplied
    headers and jwt/authentication key

    Args:
        headers (dict): session headers
        jwt (str): jwt/authentication key

    Returns:
        requests.Session: open session
    """

    session = requests.Session()
    if headers is not None:
        session.headers.update(headers)
    if jwt is not None:
        session.cookies.set("jwt", jwt)
    return session


def post_handler(session: requests.Session, url: str, json: dict,
                 params: dict = None) -> requests.Response:
    """ post_handler: handles all POST operations for Plemmy

    Args:
        session (requests.Session): open Lemmy session
        url (str): URL of API call
        json (dict): json/form data
        params (dict, optional): parameters for POST operation

    Returns:
        requests.Response: server response for POST operation
    """

    logger = logging.getLogger(__name__)
    try:
        re = session.post(url, json=json, params=params, timeout=30)
        logger.debug(f"Code: {re.status_code}")
    except requests.exceptions.RequestException as ex:
        logger.error(f"POST error: {ex}")
        return None
    return re


def put_handler(session: requests.Session, url: str, json: dict,
                params: dict = None) -> requests.Response:
    """ put_handler: handles all PUT operations for Plemmy

    Args:
        session (requests.Session): open Lemmy session
        url (str): URL of API call
        json (dict): json/form data
        params (dict, optional): parameters for PUT operation

    Returns:
        requests.Response: server response for PUT operation
    """

    logger = logging.getLogger(__name__)
    try:
        re = session.put(url, json=json, params=params, timeout=30)
        logger.debug(f"Code: {re.status_code}")
    except requests.exceptions.RequestException as ex:
        logger.error(f"PUT error: {ex}")
        return None
    return re


def get_handler(session: requests.Session, url: str, json: dict,
                params: dict = None) -> requests.Response:
    """ get_handler: handles all GET operations for Plemmy

    Args:
        session (requests.Session): open Lemmy session
        url (str): URL of API call
        json (dict): json/form data
        params (dict, optional): parameters for GET operation

    Returns:
        requests.Response: server response for GET operation
    """

    logger = logging.getLogger(__name__)
    try:
        re = session.get(url, json=json, params=params, timeout=30)
        logger.debug(f"Code: {re.status_code}")
    except requests.exceptions.RequestException as ex:
        logger.error(f"GET error: {ex}")
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
    return {k: v for k, v in arguments.items()
            if v is not None and k != "self"}
