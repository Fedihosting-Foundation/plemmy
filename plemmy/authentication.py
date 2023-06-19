import requests
import logging

API_VERSION = "v3"


class Session(object):

    def __init__(self, lemmy_server_url: str):

        self.logger = logging.getLogger(__name__)
        self.api_url = lemmy_server_url + f"/api/{API_VERSION}"
        self.token = None

    def log_in(self, username_or_email: str, password: str) -> bool:

        msg = {
            "username_or_email": username_or_email,
            "password": password,
        }

        self.logger.debug(f"Logging in as {username_or_email}")
        try:
            res = requests.post(f"{self.api_url}/user/login", json=msg)
            self.token = res.json()["jwt"]

        except Exception as ex:
            self.logger.error(f"Error logging in as {username_or_email}: {ex}")
            return False

        self.logger.debug(f"Successfully logged in as {username_or_email}")
        return True

    def log_out(self) -> None:

        self.token = None
        self.logger.debug(f"Logged out")
