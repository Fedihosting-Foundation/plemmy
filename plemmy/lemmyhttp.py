from typing import List
import logging
import requests

from .utils import post_handler, put_handler, get_handler, create_form

API_VERSION = "v3"


class LemmyHttp(object):

    def __init__(self, base_url: str, headers: dict = None) -> None:

        self._api_url = base_url + f"/api/{API_VERSION}"
        self._headers = headers
        self.key = ""
        self.logger = logging.getLogger(__name__)

    def add_admin(self, added: bool, person_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/add", self._headers, form)

    def add_mod_to_community(self, added: bool, community_id: int,
                             person_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/mod",
                            self._headers, form)

    def approve_registration_application(
            self, approve: bool, id: int, deny_reason: str = None
    ) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(
            f"{self._api_url}/admin/registration_application/approve",
            self._headers, form
        )

    def ban_from_community(self, ban: bool, community_id: int, person_id: int,
                           expires: int = None, reason: str = None,
                           remove_data: bool = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/ban_user",
                            self._headers, form)

    def ban_person(self, ban: bool, person_id: int,
                   expires: int = None, reason: str = None,
                   remove_data: bool = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/user/ban", self._headers, form)

    def block_community(self, block: bool,
                        community_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/block",
                            self._headers, form)

    def block_person(self, block: bool, person_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/user/block", self._headers, form)

    def change_password(self, new_password: str, new_password_verify: str,
                        old_password: str) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/user/change_password",
                           self._headers, form)

    def create_comment(self, content: str, post_id: int,
                       form_id: str = None, language_id: int = None,
                       parent_id: int = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment", self._headers, form)

    def create_comment_report(self, comment_id: int,
                              reason: str) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/report",
                            self._headers, form)

    def create_community(self, name: str, title: str,
                         banner: str = None, description: str = None,
                         discussion_languages: List[int] = None,
                         icon: str = None, nsfw: bool = None,
                         posting_redirect_to_mods: bool = None
                         ) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community", self._headers, form)

    def create_post(self, community_id: int, name: str, body: str = None,
                    honeypot: str = None, language_id: int = None,
                    nsfw: bool = None, url: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post", self._headers, form)

    def create_post_report(self, post_id: int,
                           reason: str) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/report",
                            self._headers, form)

    def create_private_message(self, content: str,
                               recipient_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/private_message",
                            self._headers, form)

    def create_private_message_report(self, private_message_id: int,
                                      reason: str) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/private_message_report",
                            self._headers, form)

    def create_site(self, name: str, actor_name_max_length: int = None,
                    allowed_instances: List[str] = None,
                    application_email_admins: bool = None,
                    application_question: str = None, banner: str = None,
                    blocked_instances: List[str] = None,
                    captcha_difficulty: str = None,
                    captcha_enabled: bool = None,
                    community_creation_admin_only: bool = None,
                    default_post_listing_type: str = None,
                    default_theme: str = None, description: str = None,
                    discussion_languages: List[int] = None,
                    enable_downvotes: bool = None, enable_nsfw: bool = None,
                    federation_debug: bool = None,
                    federation_enabled: bool = None,
                    federation_worker_count: int = None,
                    hide_modlog_mod_names: bool = None, icon: str = None,
                    legal_information: str = None,
                    private_instance: bool = None,
                    rate_limit_comment: int = None,
                    rate_limit_comment_per_second: int = None,
                    rate_limit_image: int = None,
                    rate_limit_image_per_second: int = None,
                    rate_limit_message: int = None,
                    rate_limit_message_per_second: int = None,
                    rate_limit_post: int = None,
                    rate_limit_post_per_second: int = None,
                    rate_limit_register: int = None,
                    rate_limit_register_per_second: int = None,
                    rate_limit_search: int = None,
                    rate_limit_search_per_second: int = None,
                    registration_mode: str = None,
                    reports_email_admins: bool = None,
                    require_email_verification: bool = None,
                    sidebar: str = None, slur_filter_regex: str = None,
                    taglines: List[str] = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/site", self._headers, form)

    def delete_account(self, password: str) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/user/delete_account",
                            self._headers, form)

    def delete_comment(self, comment_id: int,
                       deleted: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/delete",
                            self._headers, form)

    def delete_community(self, community_id: int,
                         deleted: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/delete",
                            self._headers, form)

    def delete_post(self, deleted: bool, post_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/delete",
                            self._headers, form)

    def delete_private_message(self, deleted: bool,
                               private_message_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/private_message/delete",
                            self._headers, form)

    def edit_comment(self, comment_id: int, content: str = None,
                     distinguished: bool = None, form_id: str = None,
                     language_id: int = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/comment", self._headers, form)

    def edit_community(self, community_id: int, banner: str = None,
                       description: str = None,
                       discussion_languages: List[int] = None,
                       icon: str = None, nsfw: bool = None,
                       posting_restricted_to_mods: bool = None,
                       title: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/post", self._headers, form)

    def edit_post(self, post_id: int, body: str = None,
                  language_id: int = None, name: str = None, nsfw: bool = None,
                  url: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/post", self._headers, form)

    def edit_private_message(self, content: str,
                             private_message_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/private_message",
                           self._headers, form)

    def edit_site(self, actor_name_max_length: int = None,
                  allowed_instances: List[str] = None,
                  application_email_admins: bool = None,
                  application_question: str = None, banner: str = None,
                  blocked_instances: List[str] = None,
                  captcha_difficulty: str = None, captcha_enabled: bool = None,
                  community_creation_admin_only: bool = None,
                  default_post_listing_type: str = None,
                  default_theme: str = None,
                  description: str = None,
                  discussion_languages: List[int] = None,
                  enable_downvotes: bool = None, enable_nsfw: bool = None,
                  federation_debug: bool = None,
                  federation_enabled: bool = None,
                  federation_worker_count: int = None,
                  hide_modlog_mod_names: bool = None, icon: str = None,
                  legal_information: str = None, name: str = None,
                  private_instance: bool = None,
                  rate_limit_comment: int = None,
                  rate_limit_comment_per_second: int = None,
                  rate_limit_image: int = None,
                  rate_limit_image_per_second: int = None,
                  rate_limit_message: int = None,
                  rate_limit_message_per_second: int = None,
                  rate_limit_post: int = None,
                  rate_limit_post_per_second: int = None,
                  rate_limit_register: int = None,
                  rate_limit_register_per_second: int = None,
                  rate_limit_search: int = None,
                  rate_limit_search_per_second: int = None,
                  registration_mode: str = None,
                  reports_email_admins: bool = None,
                  require_email_verification: bool = None, sidebar: str = None,
                  slur_filter_regex: str = None,
                  taglines: List[str] = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/site", self._headers, form)

    def feature_post(self, feature_type: str, featured: bool,
                     post_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/feature",
                            self._headers, form)

    def follow_community(self, community_id: int,
                         follow: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/follow",
                            self._headers, form)

    def get_banned_persons(self) -> requests.Response:

        form = {"auth": self.key}
        return get_handler(f"{self._api_url}/user/banned", self._headers, form)

    def get_captcha(self) -> requests.Response:

        return get_handler(f"{self._api_url}/user/get_captcha",
                           self._headers, {})

    def get_comments(self, community_id: str = None,
                     community_name: str = None, limit: int = None,
                     max_depth: int = None, page: int = None,
                     parent_id: int = None, post_id: int = None,
                     saved_only: bool = None, sort: str = None,
                     type_: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/comment/list",
                           self._headers, form)

    def get_community(self, id: int = None,
                      name: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/community", self._headers, form)

    def get_modlog(self, type_: str, community_id: int = None,
                   limit: int = None, mod_person_id: int = None,
                   other_person_id: int = None,
                   page: int = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/modlog", self._headers, form)

    def get_person_details(self, community_id: int = None, limit: int = None,
                           page: int = None, person_id: int = None,
                           saved_only: bool = None, sort: str = None,
                           username: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/user", self._headers, form)

    def get_person_mentions(self, limit: int = None, page: int = None,
                            sort: str = None,
                            unread_only: bool = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/user/mention",
                           self._headers, form)

    def get_post(self, comment_id: int = None,
                 id: int = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/post", self._headers, form)

    def get_posts(self, community_id: int = None, community_name: str = None,
                  limit: int = None, page: int = None, saved_only: bool = None,
                  sort: str = None,
                  type_: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/post/list", self._headers, form)

    def get_private_messages(self, limit: int = None, page: int = None,
                             unread_only: bool = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/private_message/list",
                           self._headers, form)

    def get_replies(self, limit: int = None, page: int = None,
                    sort: str = None,
                    unread_only: bool = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/user/replies",
                           self._headers, form)

    def get_report_count(self, community_id: int = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
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

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/like",
                            self._headers, form)

    def like_post(self, post_id: int, score: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/like", self._headers, form)

    def list_comment_reports(self, community_id: int = None, limit: int = None,
                             page: int = None, unresolved_only: bool = None
                             ) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/comment/report/list",
                           self._headers, form)

    def list_communities(self, limit: int = None, page: int = None,
                         sort: str = None,
                         type_: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/community/list",
                           self._headers, form)

    def list_post_reports(self, community_id: int = None, limit: int = None,
                          page: int = None, unresolved_only: bool = None
                          ) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/post/report/list",
                           self._headers, form)

    def list_private_message_reports(self, limit: int = None, page: int = None,
                                     unresolved_only: bool = None
                                     ) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/private_message/report/list",
                           self._headers, form)

    def list_registration_applications(self, limit: int = None,
                                       page: int = None,
                                       unread_only: bool = None
                                       ) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(
            f"{self._api_url}/admin/registration_application/list",
            self._headers, form
        )

    def lock_post(self, locked: bool, post_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/lock", self._headers, form)

    def login(self, username_or_email: str,
              password: str) -> requests.Response:

        form = create_form(locals())
        re = post_handler(f"{self._api_url}/user/login", self._headers, form)
        self.key = re.json()["jwt"]
        return re

    def mark_all_as_read(self) -> requests.Response:

        form = {"auth": self.key}
        return post_handler(f"{self._api_url}/user/mark_all_as_read",
                            self._headers, form)

    def mark_comment_reply_as_read(self, comment_reply_id: int,
                                   read: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/mark_as_read",
                            self._headers, form)

    def mark_person_mention_as_read(self, person_mention_id: int,
                                    read: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/user/mention/mark_as_read",
                            self._headers, form)

    def mark_post_as_read(self, post_id: int, read: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/mark_as_read",
                            self._headers, form)

    def mark_private_message_as_read(self, private_message_id: int,
                                     read: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/private_message/mark_as_read",
                            self._headers, form)

    def password_change(self, password: str, password_verify: str,
                        token: str) -> requests.Response:

        form = create_form(locals())
        return post_handler(f"{self._api_url}/user/password_change",
                            self._headers, form)

    def password_reset(self, email: str) -> requests.Response:

        form = {"email": email}
        return post_handler(f"{self._api_url}/user/password_reset",
                            self._headers, form)

    def purge_comment(self, comment_id: int,
                      reason: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/purge/comment",
                            self._headers, form)

    def purge_community(self, community_id: int,
                        reason: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/purge/community",
                            self._headers, form)

    def purge_person(self, person_id: int,
                     reason: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/purge/person",
                            self._headers, form)

    def purge_post(self, post_id: int,
                   reason: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/purge/post",
                            self._headers, form)

    def register(self, password: str, password_verify: str, show_nsfw: bool,
                 username: str, answer: str = None, captcha_answer: str = None,
                 captcha_uuid: str = None, email: str = None,
                 honeypot: str = None) -> requests.Response:

        form = create_form(locals())
        return post_handler(f"{self._api_url}/user/register",
                            self._headers, form)

    def remove_comment(self, comment_id: int, removed: bool,
                       reason: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/remove",
                            self._headers, form)

    def remove_community(self, community_id: int, removed: bool,
                         expires: int = None,
                         reason: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/remove",
                            self._headers, form)

    def remove_post(self, post_id: int, removed: bool,
                    reason: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/remove",
                            self._headers, form)

    def resolve_comment_report(self, report_id: int,
                               resolved: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/comment/report/resolve",
                           self._headers, form)

    def resolve_object(self, q: str) -> requests.Response:

        form = {"q": q, "auth": self.key}
        return get_handler(f"{self._api_url}/resolve_object",
                           self._headers, form)

    def resolve_post_report(self, report_id: int,
                            resolved: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/post/report/resolve",
                           self._headers, form)

    def resolve_private_message_report(self, report_id: int,
                                       resolved: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/private_message/report/resolve",
                           self._headers, form)

    def save_comment(self, comment_id: int, save: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/comment/save",
                           self._headers, form)

    def save_post(self, post_id: int, save: bool) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/post/save", self._headers, form)

    def save_user_settings(self, avatar: str = None, banner: str = None,
                           bio: str = None, bot_account: bool = None,
                           default_listing_type: str = None,
                           default_sort_type: str = None,
                           discussion_languages: List[int] = None,
                           display_name: str = None, email: str = None,
                           interface_language: str = None,
                           matrix_user_id: str = None,
                           send_notifications_to_email: bool = None,
                           show_avatars: bool = None,
                           show_bot_accounts: bool = None,
                           show_new_post_notifs: bool = None,
                           show_nsfw: bool = None,
                           show_read_posts: bool = None,
                           show_scores: bool = None,
                           theme: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/user/save_user_settings",
                           self._headers, form)

    def search(self, q: str, community_id: str = None,
               community_name: str = None, creator_id: int = None,
               limit: int = None, listing_type: str = None, page: int = None,
               sort: str = None, type_: str = None) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/search", self._headers, form)

    def transfer_community(self, community_id: int,
                           person_id: int) -> requests.Response:

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/transfer",
                            self._headers, form)

    def verify_email(self, token: str) -> requests.Response:

        form = {"token": token}
        return post_handler(f"{self._api_url}/user/verify_email",
                            self._headers, form)
