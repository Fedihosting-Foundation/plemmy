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

    def create_post_report(self, post_id: int,
                           reason: str) -> requests.Response:

        form = {
            "auth": self.key,
            "post_id": post_id,
            "reason": reason
        }
        return post_handler(f"{self._api_url}/post/report",
                            self._headers, form)

    def create_private_message(self, content: str,
                               recipient_id: int) -> requests.Response:

        form = {
            "auth": self.key,
            "content": content,
            "recipient_id": recipient_id
        }
        return post_handler(f"{self._api_url}/private_message",
                            self._headers, form)

    def create_private_message_report(self, private_message_id: int,
                                      reason: str) -> requests.Response:

        form = {
            "auth": self.key,
            "private_message_id": private_message_id,
            "reason": reason
        }
        return post_handler(f"{self._api_url}/private_message_report",
                            self._headers, form)

    def create_site(self, name: str, actor_name_max_length: int = -1,
                    allowed_instances: List[str] = [],
                    application_email_admins: bool = False,
                    application_question: str = "", banner: str = "",
                    blocked_instances: List[str] = [],
                    captcha_difficulty: str = "",
                    captcha_enabled: bool = False,
                    community_creation_admin_only: bool = False,
                    default_post_listing_type: str = "",
                    default_theme: str = "", description: str = "",
                    discussion_languages: List[int] = [],
                    enable_downvotes: bool = True, enable_nsfw: bool = False,
                    federation_debug: bool = False,
                    federation_enabled: bool = True,
                    federation_worker_count: int = -1,
                    hide_modlog_mod_names: bool = False, icon: str = "",
                    legal_information: str = "",
                    private_instance: bool = False,
                    rate_limit_comment: int = -1,
                    rate_limit_comment_per_second: int = -1,
                    rate_limit_image: int = -1,
                    rate_limit_image_per_second: int = -1,
                    rate_limit_message: int = -1,
                    rate_limit_message_per_second: int = -1,
                    rate_limit_post: int = -1,
                    rate_limit_post_per_second: int = -1,
                    rate_limit_register: int = -1,
                    rate_limit_register_per_second: int = -1,
                    rate_limit_search: int = -1,
                    rate_limit_search_per_second: int = -1,
                    registration_mode: str = "open",
                    reports_email_admins: bool = False,
                    require_email_verification: bool = False,
                    sidebar: str = "", slur_filter_regex: str = "",
                    taglines: List[str] = []) -> requests.Response:

        form = {
            "actor_name_max_length": actor_name_max_length,
            "allowed_instances": allowed_instances,
            "application_email_admins": application_email_admins,
            "application_question": application_question,
            "auth": self.key,
            "banner": banner,
            "blocked_instances": blocked_instances,
            "captcha_difficulty": captcha_difficulty,
            "captcha_enabled": captcha_enabled,
            "community_creation_admin_only": community_creation_admin_only,
            "default_post_listing_type": default_post_listing_type,
            "default_theme": default_theme,
            "description": description,
            "discussion_languages": discussion_languages,
            "enable_downvotes": enable_downvotes,
            "enable_nsfw": enable_nsfw,
            "federation_debug": federation_debug,
            "federation_enabled": federation_enabled,
            "federation_worker_count": federation_worker_count,
            "hide_modlog_mod_names": hide_modlog_mod_names,
            "icon": icon,
            "legal_information": legal_information,
            "name": name,
            "private_instance": private_instance,
            "rate_limit_comment": rate_limit_comment,
            "rate_limit_comment_per_second": rate_limit_comment_per_second,
            "rate_limit_image": rate_limit_image,
            "rate_limit_image_per_second": rate_limit_image_per_second,
            "rate_limit_message": rate_limit_message,
            "rate_limit_message_per_second": rate_limit_message_per_second,
            "rate_limit_post": rate_limit_post,
            "rate_limit_post_per_second": rate_limit_post_per_second,
            "rate_limit_register": rate_limit_register,
            "rate_limit_register_per_second": rate_limit_register_per_second,
            "rate_limit_search": rate_limit_search,
            "rate_limit_search_per_second": rate_limit_search_per_second,
            "registration_mode": registration_mode,
            "reports_email_admins": reports_email_admins,
            "require_email_verification": require_email_verification,
            "sidebar": sidebar,
            "slur_filter_regex": slur_filter_regex,
            "taglines": taglines
        }
        return post_handler(f"{self._api_url}/site", self._headers, form)

    def delete_account(self, password: str) -> requests.Response:

        form = {
            "auth": self.key,
            "password": password
        }
        return post_handler(f"{self._api_url}/user/delete_account",
                            self._headers, form)

    def delete_comment(self, comment_id: int,
                       deleted: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "comment_id": comment_id,
            "deleted": deleted
        }
        return post_handler(f"{self._api_url}/comment/delete",
                            self._headers, form)

    def delete_community(self, community_id: int,
                         deleted: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "deleted": deleted
        }
        return post_handler(f"{self._api_url}/community/delete",
                            self._headers, form)

    def delete_post(self, deleted: bool, post_id: int) -> requests.Response:

        form = {
            "auth": self.key,
            "deleted": deleted,
            "post_id": post_id
        }
        return post_handler(f"{self._api_url}/post/delete",
                            self._headers, form)

    def delete_private_message(self, deleted: bool,
                               private_message_id: int) -> requests.Response:

        form = {
            "auth": self.key,
            "deleted": deleted,
            "private_message_id": private_message_id
        }
        return post_handler(f"{self._api_url}/private_message/delete",
                            self._headers, form)

    def edit_comment(self, comment_id: int, content: str = "",
                     distinguished: bool = False, form_id: str = "",
                     language_id: int = -1) -> requests.Response:

        form = {
            "auth": self.key,
            "comment_id": comment_id,
            "content": content,
            "distinguished": distinguished,
            "form_id": form_id,
            "language_id": language_id
        }
        return put_handler(f"{self._api_url}/comment", self._headers, form)

    def edit_community(self, community_id: int, banner: str = "",
                       description: str = "",
                       discussion_languages: List[int] = [], icon: str = "",
                       nsfw: bool = False,
                       posting_restricted_to_mods: bool = False,
                       title: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "banner": banner,
            "community_id": community_id,
            "description": description,
            "discussion_languages": discussion_languages,
            "icon": icon,
            "nsfw": nsfw,
            "posting_restricted_to_mods": posting_restricted_to_mods,
            "title": title,
        }
        return put_handler(f"{self._api_url}/post", self._headers, form)

    def edit_post(self, post_id: int, body: str = "", language_id: int = -1,
                  name: str = "", nsfw: bool = False,
                  url: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "body": body,
            "language_id": language_id,
            "name": name,
            "nsfw": nsfw,
            "post_id": post_id,
            "url": url
        }
        return put_handler(f"{self._api_url}/post", self._headers, form)

    def edit_private_message(self, content: str,
                             private_message_id: int) -> requests.Response:

        form = {
            "auth": self.key,
            "content": content,
            "private_message_id": private_message_id
        }
        return put_handler(f"{self._api_url}/private_message",
                           self._headers, form)

    def edit_site(self, actor_name_max_length: int = -1,
                  allowed_instances: List[str] = [],
                  application_email_admins: bool = False,
                  application_question: str = "", banner: str = "",
                  blocked_instances: List[str] = [],
                  captcha_difficulty: str = "", captcha_enabled: bool = False,
                  community_creation_admin_only: bool = False,
                  default_post_listing_type: str = "", default_theme: str = "",
                  description: str = "", discussion_languages: List[int] = [],
                  enable_downvotes: bool = True, enable_nsfw: bool = False,
                  federation_debug: bool = False,
                  federation_enabled: bool = True,
                  federation_worker_count: int = -1,
                  hide_modlog_mod_names: bool = False, icon: str = "",
                  legal_information: str = "", name: str = "",
                  private_instance: bool = False, rate_limit_comment: int = -1,
                  rate_limit_comment_per_second: int = -1,
                  rate_limit_image: int = -1,
                  rate_limit_image_per_second: int = -1,
                  rate_limit_message: int = -1,
                  rate_limit_message_per_second: int = -1,
                  rate_limit_post: int = -1,
                  rate_limit_post_per_second: int = -1,
                  rate_limit_register: int = -1,
                  rate_limit_register_per_second: int = -1,
                  rate_limit_search: int = -1,
                  rate_limit_search_per_second: int = -1,
                  registration_mode: str = "open",
                  reports_email_admins: bool = False,
                  require_email_verification: bool = False, sidebar: str = "",
                  slur_filter_regex: str = "",
                  taglines: List[str] = []) -> requests.Response:

        form = {
            "actor_name_max_length": actor_name_max_length,
            "allowed_instances": allowed_instances,
            "application_email_admins": application_email_admins,
            "application_question": application_question,
            "auth": self.key,
            "banner": banner,
            "blocked_instances": blocked_instances,
            "captcha_difficulty": captcha_difficulty,
            "captcha_enabled": captcha_enabled,
            "community_creation_admin_only": community_creation_admin_only,
            "default_post_listing_type": default_post_listing_type,
            "default_theme": default_theme,
            "description": description,
            "discussion_languages": discussion_languages,
            "enable_downvotes": enable_downvotes,
            "enable_nsfw": enable_nsfw,
            "federation_debug": federation_debug,
            "federation_enabled": federation_enabled,
            "federation_worker_count": federation_worker_count,
            "hide_modlog_mod_names": hide_modlog_mod_names,
            "icon": icon,
            "legal_information": legal_information,
            "name": name,
            "private_instance": private_instance,
            "rate_limit_comment": rate_limit_comment,
            "rate_limit_comment_per_second": rate_limit_comment_per_second,
            "rate_limit_image": rate_limit_image,
            "rate_limit_image_per_second": rate_limit_image_per_second,
            "rate_limit_message": rate_limit_message,
            "rate_limit_message_per_second": rate_limit_message_per_second,
            "rate_limit_post": rate_limit_post,
            "rate_limit_post_per_second": rate_limit_post_per_second,
            "rate_limit_register": rate_limit_register,
            "rate_limit_register_per_second": rate_limit_register_per_second,
            "rate_limit_search": rate_limit_search,
            "rate_limit_search_per_second": rate_limit_search_per_second,
            "registration_mode": registration_mode,
            "reports_email_admins": reports_email_admins,
            "require_email_verification": require_email_verification,
            "sidebar": sidebar,
            "slur_filter_regex": slur_filter_regex,
            "taglines": taglines
        }
        return put_handler(f"{self._api_url}/site", self._headers, form)

    def feature_post(self, feature_type: str, featured: bool,
                     post_id: int) -> requests.Response:

        form = {
            "auth": self.key,
            "feature_type": feature_type,
            "featured": bool,
            "post_id": post_id
        }
        return post_handler(f"{self._api_url}/post/feature",
                            self._headers, form)

    def follow_community(self, community_id: int,
                         follow: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "follow": follow
        }
        return post_handler(f"{self._api_url}/community/follow")

    def get_banned_persons(self) -> requests.Response:

        form = {"auth": self.key}
        return get_handler(f"{self._api_url}/user/banned", self._headers, form)

    def get_captcha(self) -> requests.Response:

        return get_handler(f"{self._api_url}/user/get_captcha",
                           self._headers, {})

    def get_comments(self, community_id: str = "", community_name: str = "",
                     limit: int = -1, max_depth: int = -1, page: int = -1,
                     parent_id: int = -1, post_id: int = -1,
                     saved_only: bool = False, sort: str = "Hot",
                     type_: str = "All") -> requests.Response:

        form = {
            "auth": self._api_url,
            "community_id": community_id,
            "community_name": community_name,
            "limit": limit,
            "max_depth": max_depth,
            "page": page,
            "parent_id": parent_id,
            "post_id": post_id,
            "saved_only": saved_only,
            "sort": sort,
            "type_": type_
        }
        return get_handler(f"{self._api_url}/comment/list",
                           self._headers, form)

    def get_community(self, id: int = -1, name: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "id": id,
            "name": name
        }
        return get_handler(f"{self._api_url}/community", self._headers, form)

    def get_modlog(self, type_: str, community_id: int = -1, limit: int = -1,
                   mod_person_id: int = -1, other_person_id: int = -1,
                   page: int = -1) -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "limit": limit,
            "mod_person_id": mod_person_id,
            "other_person_id": other_person_id,
            "page": page,
            "type_": type_
        }
        return get_handler(f"{self._api_url}/modlog", self._headers, form)

    def get_person_details(self, community_id: int = -1, limit: int = -1,
                           page: int = -1, person_id: int = -1,
                           saved_only: bool = False, sort: str = "Active",
                           username: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "limit": limit,
            "page": page,
            "person_id": person_id,
            "saved_only": saved_only,
            "sort": sort,
            "username": username
        }
        return get_handler(f"{self._api_url}/user", self._headers, form)

    def get_person_mentions(self, limit: int = -1, page: int = -1,
                            sort: str = "Active",
                            unread_only: bool = False) -> requests.Response:

        form = {
            "auth": self.key,
            "limit": limit,
            "page": page,
            "sort": sort,
            "unread_only": unread_only
        }
        return get_handler(f"{self._api_url}/user/mention",
                           self._headers, form)

    def get_post(self, comment_id: int = -1,
                 id: int = -1) -> requests.Response:

        form = {
            "auth": self.key,
            "comment_id": comment_id,
            "id": id
        }
        return get_handler(f"{self._api_url}/post", self._headers, form)

    def get_posts(self, community_id: int = -1, community_name: str = "",
                  limit: int = -1, page: int = -1, saved_only: bool = False,
                  sort: str = "Active",
                  type_: str = "All") -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "community_name": community_name,
            "limit": limit,
            "page": page,
            "saved_only": saved_only,
            "sort": sort,
            "type_": type_
        }
        return get_handler(f"{self._api_url}/post/list", self._headers, form)

    def get_private_messages(self, limit: int = -1, page: int = -1,
                             unread_only: bool = False) -> requests.Response:

        form = {
            "auth": self.key,
            "limit": limit,
            "page": page,
            "unread_only": unread_only
        }
        return get_handler(f"{self._api_url}/private_message/list",
                           self._headers, form)

    def get_replies(self, limit: int = -1, page: int = -1, sort: str = "New",
                    unread_only: bool = False) -> requests.Response:

        form = {
            "auth": self.key,
            "limit": limit,
            "page": page,
            "sort": sort,
            "unread_only": unread_only
        }
        return get_handler(f"{self._api_url}/user/replies",
                           self._headers, form)

    def get_report_count(self, community_id: int = -1) -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id
        }
        return get_handler(f"{self._api_url}/user/report_count",
                           self._headers, form)

    def get_site(self) -> requests.Response:

        form = {"auth": self.key}
        return get_handler(f"{self._api_url}/site", self._headers, form)

    def get_site_metadata(self, url: str) -> requests.Response:

        form = {"url": url}
        return get_handler(f"{self._api_url}/post/site_metadata",
                           self._headers, form)

    def get_unread_count(self) -> requests.Response:

        form = {"auth": self.key}
        return get_handler(f"{self._api_url}/user/unread_count",
                           self._headers, form)

    def get_unread_registration_application_count(self) -> requests.Response:

        form = {"auth": self.key}
        return get_handler(
            f"{self._api_url}/admin/registration_application/count",
            self._headers, form
        )

    def leave_admin(self) -> requests.Response:

        form = {"auth": self.key}
        return post_handler(f"{self._api_url}/user/leave_admin",
                            self._headers, form)

    def like_comment(self, comment_id: int, score: int) -> requests.Response:

        form = {
            "auth": self.key,
            "comment_id": comment_id,
            "score": score
        }
        return post_handler(f"{self._api_url}/comment/like",
                            self._headers, form)

    def like_post(self, post_id: int, score: int) -> requests.Response:

        form = {
            "auth": self.key,
            "post_id": post_id,
            "score": score
        }
        return post_handler(f"{self._api_url}/post/like", self._headers, form)

    def list_comment_reports(self, community_id: int = -1, limit: int = -1,
                             page: int = -1, unresolved_only: bool = False
                             ) -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "limit": limit,
            "page": page,
            "unresolved_only": unresolved_only
        }
        return get_handler(f"{self._api_url}/comment/report/list",
                           self._headers, form)

    def list_communities(self, limit: int = -1, page: int = -1,
                         sort: str = "Active",
                         type_: str = "All") -> requests.Response:

        form = {
            "auth": self.key,
            "limit": limit,
            "page": page,
            "sort": sort,
            "type_": type_
        }
        return get_handler(f"{self._api_url}/community/list",
                           self._headers, form)

    def list_post_reports(self, community_id: int = -1, limit: int = -1,
                          page: int = -1, unresolved_only: bool = False
                          ) -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "limit": limit,
            "page": page,
            "unresolved_only": unresolved_only
        }
        return get_handler(f"{self._api_url}/post/report/list",
                           self._headers, form)

    def list_private_message_reports(self, limit: int = -1, page: int = -1,
                                     unresolved_only: bool = False
                                     ) -> requests.Response:

        form = {
            "auth": self.key,
            "limit": limit,
            "page": page,
            "unresolved_only": unresolved_only
        }
        return get_handler(f"{self._api_url}/private_message/report/list",
                           self._headers, form)

    def list_registration_applications(self, limit: int = -1, page: int = -1,
                                       unread_only: bool = False
                                       ) -> requests.Response:

        form = {
            "auth": self.key,
            "limit": limit,
            "page": page,
            "unread_only": unread_only
        }
        return get_handler(
            f"{self._api_url}/admin/registration_application/list",
            self._headers, form
        )

    def lock_post(self, locked: bool, post_id: int) -> requests.Response:

        form = {
            "auth": self.key,
            "locked": locked,
            "post_id": post_id
        }
        return post_handler(f"{self._api_url}/post/lock", self._headers, form)

    def login(self, username_or_email: str,
              password: str) -> requests.Response:

        form = {
            "username_or_email": username_or_email,
            "password": password
        }
        re = post_handler(f"{self._api_url}/user/login", self._headers, form)
        self.key = re.json()["jwt"]
        return re

    def mark_all_as_read(self) -> requests.Response:

        form = {"auth": self.key}
        return post_handler(f"{self._api_url}/user/mark_all_as_read",
                            self._headers, form)

    def mark_comment_reply_as_read(self, comment_reply_id: int,
                                   read: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "comment_reply_id": comment_reply_id,
            "read": read
        }
        return post_handler(f"{self._api_url}/comment/mark_as_read",
                            self._headers, form)

    def mark_person_mention_as_read(self, person_mention_id: int,
                                    read: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "person_mention_id": person_mention_id,
            "read": read
        }
        return post_handler(f"{self._api_url}/user/mention/mark_as_read",
                            self._headers, form)

    def mark_post_as_read(self, post_id: int, read: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "post_id": post_id,
            "read": read
        }
        return post_handler(f"{self._api_url}/post/mark_as_read",
                            self._headers, form)

    def mark_private_message_as_read(self, private_message_id: int,
                                     read: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "private_message_id": private_message_id,
            "read": read
        }
        return post_handler(f"{self._api_url}/private_message/mark_as_read",
                            self._headers, form)

    def password_change(self, password: str, password_verify: str,
                        token: str) -> requests.Response:

        form = {
            "password": password,
            "password_verify": password_verify,
            "token": token
        }
        return post_handler(f"{self._api_url}/user/password_change",
                            self._headers, form)

    def password_reset(self, email: str) -> requests.Response:

        form = {"email": email}
        return post_handler(f"{self._api_url}/user/password_reset",
                            self._headers, form)

    def purge_comment(self, comment_id: int,
                      reason: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "comment_id": comment_id,
            "reason": reason
        }
        return post_handler(f"{self._api_url}/admin/purge/comment",
                            self._headers, form)

    def purge_community(self, community_id: int,
                        reason: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "reason": reason
        }
        return post_handler(f"{self._api_url}/admin/purge/community",
                            self._headers, form)

    def purge_person(self, person_id: int,
                     reason: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "person_id": person_id,
            "reason": reason
        }
        return post_handler(f"{self._api_url}/admin/purge/person",
                            self._headers, form)

    def purge_post(self, post_id: int, reason: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "post_id": post_id,
            "reason": reason
        }
        return post_handler(f"{self._api_url}/admin/purge/post",
                            self._headers, form)

    def register(self, password: str, password_verify: str, show_nsfw: bool,
                 username: str, answer: str = "", captcha_answer: str = "",
                 captcha_uuid: str = "", email: str = "",
                 honeypot: str = "") -> requests.Response:

        form = {
            "answer": answer,
            "captcha_answer": captcha_answer,
            "captcha_uuid": captcha_uuid,
            "email": email,
            "honeypot": honeypot,
            "password": password,
            "password_verify": password_verify,
            "show_nsfw": show_nsfw,
            "username": username
        }
        return post_handler(f"{self._api_url}/user/register",
                            self._headers, form)

    def remove_comment(self, comment_id: int, removed: bool,
                       reason: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "comment_id": comment_id,
            "reason": reason,
            "removed": removed
        }
        return post_handler(f"{self._api_url}/comment/remove",
                            self._headers, form)

    def remove_community(self, community_id: int, removed: bool,
                         expires: int = -1,
                         reason: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "expires": expires,
            "reason": reason,
            "removed": removed
        }
        return post_handler(f"{self._api_url}/community/remove",
                            self._headers, form)

    def remove_post(self, post_id: int, removed: bool,
                    reason: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "post_id": post_id,
            "reason": reason,
            "removed": removed
        }
        return post_handler(f"{self._api_url}/post/remove",
                            self._headers, form)

    def resolve_comment_report(self, report_id: int,
                               resolved: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "report_id": report_id,
            "resolved": resolved
        }
        return put_handler(f"{self._api_url}/comment/report/resolve",
                           self._headers, form)

    def resolve_object(self, q: str) -> requests.Response:

        form = {
            "auth": self.key,
            "q": q
        }
        return get_handler(f"{self._api_url}/resolve_object",
                           self._headers, form)

    def resolve_post_report(self, report_id: int,
                            resolved: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "report_id": report_id,
            "resolved": resolved
        }
        return put_handler(f"{self._api_url}/post/report/resolve",
                           self._headers, form)

    def resolve_private_message_report(self, report_id: int,
                                       resolved: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "report_id": report_id,
            "resolved": resolved
        }
        return put_handler(f"{self._api_url}/private_message/report/resolve",
                           self._headers, form)

    def save_comment(self, comment_id: int, save: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "comment_id": comment_id,
            "save": save
        }
        return put_handler(f"{self._api_url}/comment/save",
                           self._headers, form)

    def save_post(self, post_id: int, save: bool) -> requests.Response:

        form = {
            "auth": self.key,
            "post_id": post_id,
            "save": save
        }
        return put_handler(f"{self._api_url}/post/save", self._headers, form)

    def save_user_settings(self, avatar: str = "", banner: str = "",
                           bio: str = "", bot_account: bool = False,
                           default_listing_type: str = "All",
                           default_sort_type: str = "Active",
                           discussion_languages: List[int] = [],
                           display_name: str = "", email: str = "",
                           interface_language: str = "",
                           matrix_user_id: str = "",
                           send_notifications_to_email: bool = False,
                           show_avatars: bool = False,
                           show_bot_accounts: bool = False,
                           show_new_post_notifs: bool = False,
                           show_nsfw: bool = False,
                           show_read_posts: bool = True,
                           show_scores: bool = True,
                           theme: str = "") -> requests.Response:

        form = {
            "auth": self.key,
            "avatar": avatar,
            "banner": banner,
            "bio": bio,
            "bot_account": bot_account,
            "default_listing_type": default_listing_type,
            "default_sort_type": default_sort_type,
            "discussion_languages": discussion_languages,
            "display_name": display_name,
            "email": email,
            "interface_language": interface_language,
            "matrix_user_id": matrix_user_id,
            "send_notifications_to_email": send_notifications_to_email,
            "show_avatars": show_avatars,
            "show_bot_accounts": show_bot_accounts,
            "show_new_post_notifs": show_new_post_notifs,
            "show_nsfw": show_nsfw,
            "show_read_posts": show_read_posts,
            "show_scores": show_scores,
            "theme": theme
        }
        return put_handler(f"{self._api_url}/user/save_user_settings",
                           self._headers, form)

    def search(self, q: str, community_id: str = "", community_name: str = "",
               creator_id: int = -1, limit: int = -1,
               listing_type: str = "All", page: int = -1, sort: str = "Active",
               type_: str = "All") -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "community_name": community_name,
            "creator_id": creator_id,
            "limit": limit,
            "listing_type": listing_type,
            "page": page,
            "q": q,
            "sort": sort,
            "type_": type_
        }
        return get_handler(f"{self._api_url}/search", self._headers, form)

    def transfer_community(self, community_id: int,
                           person_id: int) -> requests.Response:

        form = {
            "auth": self.key,
            "community_id": community_id,
            "person_id": person_id
        }
        return post_handler(f"{self._api_url}/community/transfer",
                            self._headers, form)

    def verify_email(self, token: str) -> requests.Response:

        form = {"token": token}
        return post_handler(f"{self._api_url}/user/verify_email",
                            self._headers, form)
