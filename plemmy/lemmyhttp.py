from typing import List
import logging
import requests

from .utils import post_handler, put_handler, get_handler

API_VERSION = "v3"


class LemmyHttp(object):

    def __init__(self, base_url: str, headers: dict = None) -> None:

        self._api_url = base_url + f"/api/{API_VERSION}"
        self._headers = headers
        self.key = ""
        self.logger = logging.getLogger(__name__)

    def add_admin(self, added: bool, person_id: int) -> requests.Response:

        form = {
            "added": added,
            "auth": self.key,
            "person_id": person_id
        }
        return post_handler(f"{self._api_url}/admin/add", self._headers, form)

    def add_mod_to_community(self, added: bool, community_id: int,
                             person_id: int) -> requests.Response:

        form = {
            "added": added,
            "auth": self.key,
            "community_id": community_id,
            "person_id": person_id
        }
        return post_handler(f"{self._api_url}/community/mod",
                            self._headers, form)

    def approve_registration_application(
     self, approve: bool, id: int, deny_reason: str = "") -> requests.Response:

        form = {
            "approve": approve,
            "auth": self.key,
            "deny_reason": deny_reason,
            "id": id
        }
        return put_handler(
            f"{self._api_url}/admin/registration_application/approve",
            self._headers, form
        )

    def ban_from_community(self, ban: bool, community_id: int, person_id: int,
                           expires: int = -1, reason: str = "",
                           remove_data: bool = True) -> requests.Response:

        form = {
            "auth": self.key,
            "ban": ban,
            "community_id": community_id,
            "expires": expires,
            "person_id": person_id,
            "reason": reason,
            "remove_data": remove_data
        }
        return post_handler(f"{self._api_url}/community/ban_user",
                            self._headers, form)

    def ban_person(self, ban: bool, person_id: int,
                   expires: int = -1, reason: str = "",
                   remove_data: bool = True) -> requests.Response:

        form = {
            "auth": self.key,
            "ban": ban,
            "expires": expires,
            "person_id": person_id,
            "reason": reason,
            "remove_data": remove_data
        }
        return post_handler(f"{self._api_url}/user/ban", self._headers, form)

    def block_community(self, block: bool,
                        community_id: int) -> requests.Response:

        form = {
            "auth": self.key,
            "block": block,
            "community_id": community_id
        }
        return post_handler(f"{self._api_url}/community/block",
                            self._headers, form)

    def block_person(self, block: bool, person_id: int) -> requests.Response:

        form = {
            "auth": self.key,
            "block": block,
            "person_id": person_id
        }
        return post_handler(f"{self._api_url}/user/block", self._headers, form)

    def change_password(self, new_password: str, new_password_verify: str,
                        old_password: str) -> requests.Response:

        form = {
            "auth": self.key,
            "new_password": new_password,
            "new_password_verify": new_password_verify,
            "old_password": old_password
        }
        return put_handler(f"{self._api_url}/user/change_password",
                           self._headers, form)

    def create_comment(self, content: str, post_id: int,
                       form_id: str = "", language_id: int = -1,
                       parent_id: int = -1) -> requests.Response:

        form = {
            "auth": self.key,
            "content": content,
            "form_id": form_id,
            "language_id": language_id,
            "parent_id": parent_id,
            "post_id": post_id
        }
        return post_handler(f"{self._api_url}/comment", self._headers, form)

    def create_comment_report(self, comment_id: int,
                              reason: str) -> requests.Response:

        form = {
            "auth": self.key,
            "comment_id": comment_id,
            "reason": reason
        }
        return post_handler(f"{self._api_url}/comment/report",
                            self._headers, form)

    def create_community(self, name: str, title: str,
                         banner: str = "", description: str = "",
                         discussion_languages: List[int] = [],
                         icon: str = "", nsfw: bool = False,
                         posting_redirect_to_mods: bool = False
                         ) -> requests.Response:

        form = {
            "auth": self.key,
            "banner": banner,
            "description": description,
            "discussion_languages": discussion_languages,
            "icon": icon,
            "name": name,
            "nsfw": nsfw,
            "posting_restricted_to_mods": posting_redirect_to_mods,
            "title": title
        }
        return post_handler(f"{self._api_url}/community", self._headers, form)

    def create_post(self, community_id: int, name: str, body: str = "",
                    honeypot: str = "", language_id: int = -1,
                    nsfw: bool = False, url: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "body": body,
            "community_id": community_id,
            "honeypot": honeypot,
            "language_id": language_id,
            "name": name,
            "nsfw": nsfw,
            "url": url
        }
        return post_handler(f"{self._api_url}/post", self._headers, form)

    # TODO: the rest

    def login(self, username_or_email: str,
              password: str) -> requests.Response:

        form = {
            "username_or_email": username_or_email,
            "password": password
        }
        re = post_handler(f"{self._api_url}/user/login", self._headers, form)
        self.key = re.json()["jwt"]
        return re
