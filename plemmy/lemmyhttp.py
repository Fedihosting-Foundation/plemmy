from typing import List
import logging
import requests

from .utils import post_handler, put_handler, get_handler, create_form

API_VERSION = "v3"


class LemmyHttp(object):

    def __init__(self, base_url: str, headers: dict = None) -> None:
        """ LemmyHttp object: handles all POST, PUT, and GET operations from
        the LemmyHttp API (https://join-lemmy.org/api/classes/LemmyHttp.html)

        Args:
            base_url (str): Lemmy instance to connect to (e.g.,
                "https://lemmy.ml")
            headers (dict): optional headers

        Returns:
            None
        """

        self._api_url = base_url + f"/api/{API_VERSION}"
        self._headers = headers
        self.key = ""
        self.logger = logging.getLogger(__name__)

    def add_admin(self, added: bool, person_id: int) -> requests.Response:
        """ add_admin: add admin to Lemmy instance

        Args:
            added (bool): True if adding admin, False otherwise
            person_id (int): ID of user

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/add", self._headers, form)

    def add_mod_to_community(self, added: bool, community_id: int,
                             person_id: int) -> requests.Response:
        """ add_mod_to_community: adds a user to a community's mod list

        Args:
            added (bool): True if adding mod, False otherwise
            community_id (int): ID of the community
            person_id (int): ID of user

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/mod",
                            self._headers, form)

    def approve_registration_application(
            self, approve: bool, id: int, deny_reason: str = None
    ) -> requests.Response:
        """ approve_registration_application: approve a new user's
        registration application

        Args:
            approve (bool): True if application approved, False otherwise
            id (int): ID of the application
            deny_reason (str): reason for application denial (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(
            f"{self._api_url}/admin/registration_application/approve",
            self._headers, form
        )

    def ban_from_community(self, ban: bool, community_id: int, person_id: int,
                           expires: int = None, reason: str = None,
                           remove_data: bool = None) -> requests.Response:
        """ ban_from_community: bans a user from interacting with a community

        Args:
            ban (bool): True if banned, False otherwise
            community_id (int): ID of community
            person_id (int): ID of banned user
            exires (int): ban expire time in UNIX seconds (optional)
            reason (str): reason for ban (optional)
            remove_data (bool): removes/restores user's comments/posts for
                community (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/ban_user",
                            self._headers, form)

    def ban_person(self, ban: bool, person_id: int,
                   expires: int = None, reason: str = None,
                   remove_data: bool = None) -> requests.Response:
        """ ban_person: bans a user from the Lemmy instance

        Args:
            ban (bool): True if banned, False otherwise
            person_id (int): user to ban
            expires (int): ban expire time in UNIX seconds (optional)
            reason (str): reason for ban (optional)
            remove_data (bool): removes/restores user's comments/posts/
                communities for Lemmy instance (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/user/ban", self._headers, form)

    def block_community(self, block: bool,
                        community_id: int) -> requests.Response:
        """ block_community: block a community from this Lemmy instance

        Args:
            block (bool): True if blocked, False otherwise
            community_id (int): community to block

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/block",
                            self._headers, form)

    def block_person(self, block: bool, person_id: int) -> requests.Response:
        """ block_person: block a user from this Lemmy instance

        Args:
            block (bool): True if blocked, False otherwise
            person_id (int): user to block

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/user/block", self._headers, form)

    def change_password(self, new_password: str, new_password_verify: str,
                        old_password: str) -> requests.Response:
        """ change_password: change password for currently-logged-in user

        Args:
            new_password (str): new password
            new_password_verify (str): new password
            old_password (str): current/old password

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/user/change_password",
                           self._headers, form)

    def create_comment(self, content: str, post_id: int,
                       form_id: str = None, language_id: int = None,
                       parent_id: int = None) -> requests.Response:
        """ create_comment: create a comment on a post

        Args:
            content (str): body/text of comment
            post_id (int): post to comment on
            form_id (str): front end ID (optional)
            language_id (int): language of comment (optional)
            parent_id (int): if replying to comment, this is parent
                comment's ID

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment", self._headers, form)

    def create_comment_report(self, comment_id: int,
                              reason: str) -> requests.Response:
        """ create_comment_report: report a comment

        Args:
            comment_id (int): comment to report
            reason (str): reason for report

        Returns:
            requests.Response: result of API call
        """

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
        """ create_community: create a community on this Lemmy instance

        Args:
            name (str): name of the new community
            title (str): title of the new community
            banner (str): filepath of banner image to upload (optional)
            description (str): description of the community (optional)
            discussion_languages (List[int]): languages used by the
                community (optional)
            icon (str): filepath of icon image to upload (optional)
            nsfw (bool): True if NSFW community, False otherwise (optional)
            posting_redirect_to_mods (bool): True if only mods can post to
                this community, False otherwise (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community", self._headers, form)

    def create_custom_emoji(self, alt_text: str, category: str,
                            image_url: str, keywords: List[str],
                            shortcode: str) -> requests.Response:
        """ create_custom_emoji: create custom emoji for site

        Args:
            alt_text (str): emoji alt text
            category (str): emoji category
            image_url (str): image src for emoji
            keywords (List[str]): keywords/tags for emoji
            shortcode (str): emoji shortcode

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/custom_emoji",
                            self._headers, form)

    def create_post(self, community_id: int, name: str, body: str = None,
                    honeypot: str = None, language_id: int = None,
                    nsfw: bool = None, url: str = None) -> requests.Response:
        """ create_post: create a post in a community

        Args:
            community_id (int): ID of community to post in
            name (str): name/title of the post
            body (str): body text of post (optional)
            honeypot (str): (optional) TODO: figure out what this does!!
            language_id (int): language of the post (optional)
            nsfw (bool): True if post is NSFW, False otherwise (optional)
            url (str): URL/link to share in post (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post", self._headers, form)

    def create_post_report(self, post_id: int,
                           reason: str) -> requests.Response:
        """ create_post_report: report a post

        Args:
            post_id (int): post to report
            reason (str): reason for report

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/report",
                            self._headers, form)

    def create_private_message(self, content: str,
                               recipient_id: int) -> requests.Response:
        """ create_private_message: send someone a private message

        Args:
            content (str): content of the message
            recipient_id (int): ID of the user receiving the message

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/private_message",
                            self._headers, form)

    def create_private_message_report(self, private_message_id: int,
                                      reason: str) -> requests.Response:
        """ create_private_message_report: report a private message

        Args:
            private_message_id (int): ID of the private message
            reason (str): reason for report

        Returns:
            requests.Response: result of API call
        """

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
        """ create_site: creates a Lemmy instance

        Args:
            name (str): name of the site/instance
            actor_name_max_length (int): max. num. characters in
                usernames (optional)
            allowed_instances (List[str]): list of allowed instances (optional)
            application_email_admins (bool): if True, emails admins on new
                applications, False otherwise (optional)
            application_question (str): question being asked to the applicant
            banner (str): filepath of banner used for the site/instance
            blocked_instances (List[str]): list of blocked instances (optional)
            captcha_difficulty (str): difficulty of application
                captcha (optional)
            captcha_enabled (bool): True if captcha required for registration,
                false otherwise (optional)
            community_creation_admin_only (bool): True if only admins can
                create communities, False otherwise (optional)
            default_post_listing_type (str): "Active", "Hot", etc. (optional)
            default_theme (str): default theme to use (optional)
            description (str): description of the site/instance (optional)
            discussion_languages (List[int]): languages used on the site/
                instance (optional)
            enable_downvotes (bool): True to enable downvotes, False
                otherwise (optional)
            enable_nsfw (bool): True if NSFW allowed, False
                otherwise (optional)
            federation_debug (bool): True for debug, False otherwise (optional)
            federation_enabled (bool): True if site/instance is federated,
                False otherwise (optional)
            federation_worker_count (int): number of fetch/update
                workers (optional)
            hide_modlog_mod_names (bool): True to hide names in modlog, False
                otherwise (optional)
            icon (str): filepath of icon to be used (optional)
            legal_information (str): sidebar legal info (optional)
            private_instance (bool): True if private, False
                otherwise (optional)
            rate_limit_comment (int): rate limit for comments (optional)
            rate_limit_comment_per_second (int): rate limit for comments per
                second (optional)
            rate_limit_image (int): rate limit for image uploads (optional)
            rate_limit_image_per_second (int): rate limit for image uploads
                per second (optional)
            rate_limit_message (int): rate limit for messages (optional)
            rate_limit_message_per_second (int): rate limit for messages per
                second (optional)
            rate_limit_post (int): rate limit for new posts (optional)
            rate_limit_post_per_second (int): rate limit for new posts per
                second (optional)
            rate_limit_register (int): rate limit for new
                registrations (optional)
            rate_limit_register_per_second (int): rate limit for new
                registrations per second (optional)
            rate_limit_search (int): rate limit for searches (optional)
            rate_limit_search_per_second (int): rate limit for searches per
                second (optional)
            registration_mode (str): "open", "closed" (optional)
            reports_email_admins (bool): True to send emails to admins upon new
                report, False otherwise (optional)
            require_email_verification (bool): True to require an email
                address for new registrations, False otherwise (optional)
            sidebar (str): sidebar text (optional)
            slur_filter_regex (str): regular expression to catch unwanted
                text (optional)
            taglines (List[str]): site/instance taglines (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/site", self._headers, form)

    def delete_account(self, password: str) -> requests.Response:
        """ delete_account: deletes currently-logged-in account

        Args:
            password (str): user password

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/user/delete_account",
                            self._headers, form)

    def delete_comment(self, comment_id: int,
                       deleted: bool) -> requests.Response:
        """ delete_comment: delete a comment

        Args:
            comment_id (int): ID of comment to delete
            deleted (bool): True if deleted, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/delete",
                            self._headers, form)

    def delete_community(self, community_id: int,
                         deleted: bool) -> requests.Response:
        """ delete_community: delete a community

        Args:
            community_id (int): ID of community to delete
            deleted (bool): True if deleted, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/delete",
                            self._headers, form)

    def delete_custom_emoji(self, id: int) -> requests.Response:
        """ delete_custom_emoji: delete a site emoji

        Args:
            id (int): emoji ID

        Returns:
            requests.Response: result of API call
        """

        form = {"id": id, "auth": self.key}
        return post_handler(f"{self._api_url}/custom_emoji/delete",
                            self._headers, form)

    def delete_post(self, deleted: bool, post_id: int) -> requests.Response:
        """ delete_post: delete a post

        Args:
            deleted (bool): True if deleted, False otherwise
            post_id (int): ID of post to delete

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/delete",
                            self._headers, form)

    def delete_private_message(self, deleted: bool,
                               private_message_id: int) -> requests.Response:
        """ delete_private_message: delete a private message

        Args:
            deleted (bool): True if deleted, False otherwise
            private_message_id (int): ID of private message to delete

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/private_message/delete",
                            self._headers, form)

    def distinguish_comment(self, comment_id: int,
                            distinguished: bool) -> requests.Response:
        """ distinguish_comment: distinguish/highlight a comment

        Args:
            comment_id (int): ID of comment
            distinguished (bool): True if distinguished, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/distinguish",
                            self._headers, form)

    def edit_comment(self, comment_id: int, content: str = None,
                     form_id: str = None, language_id: int = None
                     ) -> requests.Response:
        """ edit_comment: edit a comment

        Args:
            comment_id (int): ID of comment to edit
            content (str): updated/edited content (optional)
            form_id (str): front end ID (optional)
            language_id (int): language of the comment (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/comment", self._headers, form)

    def edit_community(self, community_id: int, banner: str = None,
                       description: str = None,
                       discussion_languages: List[int] = None,
                       icon: str = None, nsfw: bool = None,
                       posting_restricted_to_mods: bool = None,
                       title: str = None) -> requests.Response:
        """ edit_community: edit a community's information/behavior

        Args:
            community_id (int): ID of community to edit
            banner (str): filepath of banner to use (optional)
            description (str): community description (optional)
            discussion_languages (List[int]): languages used in the
                community (optional)
            icon (str): filepath of icon to use (optional)
            nsfw (bool): True if NSFW community, False otherwise (optional)
            posting_restricted_to_mods (bool): True if only mods can post,
                False otherwise (optional)
            title (str): community title/name (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/community", self._headers, form)

    def edit_custom_emoji(self, alt_text: str, category: str, id: int,
                          image_url: str, keywords: List[str]
                          ) -> requests.Response:
        """ edit_custom_emoji: edits information for custom emoji

        Args:
            alt_text (str): emoji alt text
            category (str): emoji category
            id (int): ID of emoji
            image_url (str): source image for emoji
            keywords (List[str]): keywords/tags for emoji

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/custom_emoji")

    def edit_post(self, post_id: int, body: str = None,
                  language_id: int = None, name: str = None, nsfw: bool = None,
                  url: str = None) -> requests.Response:
        """ edit_post: edit a post

        Args:
            post_id (int): ID of post to edit
            body (str): text of post (optional)
            language_id (int): language of post (optional)
            name (str): name of post (optional)
            nsfw (bool): True if NSFW post, False otherwise (optional)
            url (str): URL to share in post (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/post", self._headers, form)

    def edit_private_message(self, content: str,
                             private_message_id: int) -> requests.Response:
        """ edit_private_message: edit a private message

        Args:
            content (str): content of private message
            private_message_id (int): ID of private message to edit

        Returns:
            requests.Response: result of API call
        """

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
        """ edit_site: edits a Lemmy instance

        Args:
            actor_name_max_length (int): max. num. characters in
                usernames (optional)
            allowed_instances (List[str]): list of allowed instances (optional)
            application_email_admins (bool): if True, emails admins on new
                applications, False otherwise (optional)
            application_question (str): question being asked to the applicant
            banner (str): filepath of banner used for the site/instance
            blocked_instances (List[str]): list of blocked instances (optional)
            captcha_difficulty (str): difficulty of application
                captcha (optional)
            captcha_enabled (bool): True if captcha required for registration,
                false otherwise (optional)
            community_creation_admin_only (bool): True if only admins can
                create communities, False otherwise (optional)
            default_post_listing_type (str): "Active", "Hot", etc. (optional)
            default_theme (str): default theme to use (optional)
            description (str): description of the site/instance (optional)
            discussion_languages (List[int]): languages used on the site/
                instance (optional)
            enable_downvotes (bool): True to enable downvotes, False
                otherwise (optional)
            enable_nsfw (bool): True if NSFW allowed, False
                otherwise (optional)
            federation_debug (bool): True for debug, False otherwise (optional)
            federation_enabled (bool): True if site/instance is federated,
                False otherwise (optional)
            federation_worker_count (int): number of fetch/update
                workers (optional)
            hide_modlog_mod_names (bool): True to hide names in modlog, False
                otherwise (optional)
            icon (str): filepath of icon to be used (optional)
            legal_information (str): sidebar legal info (optional)
            private_instance (bool): True if private, False
                otherwise (optional)
            rate_limit_comment (int): rate limit for comments (optional)
            rate_limit_comment_per_second (int): rate limit for comments per
                second (optional)
            rate_limit_image (int): rate limit for image uploads (optional)
            rate_limit_image_per_second (int): rate limit for image uploads
                per second (optional)
            rate_limit_message (int): rate limit for messages (optional)
            rate_limit_message_per_second (int): rate limit for messages per
                second (optional)
            rate_limit_post (int): rate limit for new posts (optional)
            rate_limit_post_per_second (int): rate limit for new posts per
                second (optional)
            rate_limit_register (int): rate limit for new
                registrations (optional)
            rate_limit_register_per_second (int): rate limit for new
                registrations per second (optional)
            rate_limit_search (int): rate limit for searches (optional)
            rate_limit_search_per_second (int): rate limit for searches per
                second (optional)
            registration_mode (str): "open", "closed" (optional)
            reports_email_admins (bool): True to send emails to admins upon new
                report, False otherwise (optional)
            require_email_verification (bool): True to require an email
                address for new registrations, False otherwise (optional)
            sidebar (str): sidebar text (optional)
            slur_filter_regex (str): regular expression to catch unwanted
                text (optional)
            taglines (List[str]): site/instance taglines (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/site", self._headers, form)

    def feature_post(self, feature_type: str, featured: bool,
                     post_id: int) -> requests.Response:
        """ feature_post: feature a post

        Args:
            feature_type (str): "Community", "Local"
            featured (bool): True if featured, False otherwise
            post_id (int): ID of post to feature

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/feature",
                            self._headers, form)

    def follow_community(self, community_id: int,
                         follow: bool) -> requests.Response:
        """ follow_community: follow a community

        Args:
            community_id (int): ID of community to follow
            follow (bool): True to follow, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/follow",
                            self._headers, form)

    def get_banned_persons(self) -> requests.Response:
        """ get_banned_persons: get a list of banned users

        Args:
            None

        Returns:
            requests.Response: result of API call
        """

        form = {"auth": self.key}
        return get_handler(f"{self._api_url}/user/banned", self._headers,
                           None, params=form)

    def get_captcha(self) -> requests.Response:
        """ get_captcha: get captcha for current user

        Args:
            None

        Returns:
            requests.Response: result of API call
        """

        return get_handler(f"{self._api_url}/user/get_captcha",
                           self._headers, None, None)

    def get_comment(self, id: int) -> requests.Response:
        """ get_comment: obtain a comment by ID

        Args:
            id (int): comment ID

        Returns:
            requests.Response: result of API call
        """

        form = {"id": id, "auth": self.key}
        return get_handler(f"{self._api_url}/comment", self._headers,
                           None, params=form)

    def get_comments(self, community_id: int = None,
                     community_name: str = None, limit: int = None,
                     max_depth: int = None, page: int = None,
                     parent_id: int = None, post_id: int = None,
                     saved_only: bool = None, sort: str = None,
                     type_: str = None) -> requests.Response:
        """ get_comments: get a list of comments

        Args:
            community_id (int): ID of community to obtain comments
                from (optional)
            community_name (str): name of community to obtain comments
                from (optional)
            limit (int): max. num. comments to obtain (optional)
            max_depth (int): max. depth of comments to obtain (optional)
            page (int): page to obtain comments from (optional)
            parent_id (int): ID of parent comment to obtain comments
                from (optional)
            post_id (int): ID of post to obtain comments from (optional)
            saved_only (bool): True to only look in saved posts, False
                otherwise (optional)
            sort (str): "Hot", "New", "Old", "Top" (optional)
            type_ (str): "All", "Community", "Subscribed", "Local" (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/comment/list",
                           self._headers, None, params=form)

    def get_community(self, id: int = None,
                      name: str = None) -> requests.Response:
        """ get_community: get a community

        Args:
            id (int): ID of community (optional)
            name (str): name of community (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/community", self._headers,
                           None, params=form)

    def get_federated_instances(self) -> requests.Response:
        """ get_federated_instances: get instances federated with this instance

        Args:
            None

        Returns:
            requests.Response: result of API call
        """

        form = {"auth": self.key}
        return get_handler(f"{self._api_url}/federated_instances",
                           self._headers, None, params=form)

    def get_modlog(self, type_: str, community_id: int = None,
                   limit: int = None, mod_person_id: int = None,
                   other_person_id: int = None,
                   page: int = None) -> requests.Response:
        """ get_modlog: obtain the moderation log

        Args:
            type_ (str): "AdminPurgeComment", "AdminPurgeCommunity",
                "AdminPurgePerson", "AdminPurgePost", "All", "ModAdd",
                "ModAddCommunity", "ModBan", "ModBanFromCommunity",
                "ModFeaturePost", "ModHideCommunity", "ModLockPost",
                "ModRemoveComment", "ModRemoveCommunity", "ModRemovePost",
                "ModTransferCommunity"
            community_id (int): ID of community to get log from (optional)
            limit (int): max. num. log entries to obtain (optional)
            mod_person_id (int): ID of moderator logs to obtain (optional)
            other_person_id (int): ID of user recipient of mod
                action (optional)
            page (int): modlog page to query (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/modlog", self._headers,
                           None, params=form)

    def get_person_details(self, community_id: int = None, limit: int = None,
                           page: int = None, person_id: int = None,
                           saved_only: bool = None, sort: str = None,
                           username: str = None) -> requests.Response:
        """ get_person_details: get information for a user

        Args:
            community_id (int): community to search (optional)
            limit (int): max. num. entries to return (optional)
            page (int): page of results to query (optional)
            person_id (int): ID of user (optional)
            saved_only (bool): True to only search saved posts, False
                otherwise (optional)
            sort (str): "Active", "Hot", "MostComments", "New", "NewComments",
                "Old", "TopAll", "TopDay", "TopMonth", "TopWeek",
                "TopYear" (optional)
            username (str): user's username (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/user", self._headers,
                           None, params=form)

    def get_person_mentions(self, limit: int = None, page: int = None,
                            sort: str = None,
                            unread_only: bool = None) -> requests.Response:
        """ get_person_mentions: obtain comments where current user is
        mentioned

        Args:
            limit (int): max. num. comments to obtain (optional)
            page (int): page of results to query (optional)
            sort (str): "Hot", "New", "Old", "Top" (optional)
            unread_only (bool): True to obtain only unread mentions, False
                otherwise (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/user/mention",
                           self._headers, None, params=form)

    def get_post(self, comment_id: int = None,
                 id: int = None) -> requests.Response:
        """ get_post: get post from post ID or comment ID

        Args:
            comment_id (int): ID of comment in post (optional)
            id (int): ID of post (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/post", self._headers,
                           None, params=form)

    def get_posts(self, community_id: int = None, community_name: str = None,
                  limit: int = None, page: int = None, saved_only: bool = None,
                  sort: str = None,
                  type_: str = None) -> requests.Response:
        """ get_posts: obtain posts from a community

        Args:
            community_id (int): ID of community (optional)
            community_name (str): name of community (optional)
            limit (int): max. num. posts to obtain (optional)
            page (int): page of results to query (optional)
            saved_only (bool): True to only get saved posts, False
                otherwise (optional)
            sort (str): "Active", "Hot", "MostComments", "New", "NewComments",
                "Old", "TopAll", "TopDay", "TopMonth", "TopWeek",
                "TopYear" (optional)
            type_ (str): "All", "Community", "Local", "Subscribed" (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/post/list", self._headers,
                           None, params=form)

    def get_private_messages(self, limit: int = None, page: int = None,
                             unread_only: bool = None) -> requests.Response:
        """ get_private_messages: get private messages

        Args:
            limit (int): max. num. messages to obtain (optional)
            page (int): page of results to query (optional)
            unread_only (bool): True to only get unread messages, False
                otherwise (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/private_message/list",
                           self._headers, None, params=form)

    def get_replies(self, limit: int = None, page: int = None,
                    sort: str = None,
                    unread_only: bool = None) -> requests.Response:
        """ get_replies: get replies for current user

        Args:
            limit (int): max. num. replies to obtain (optional)
            page (int): page of results to query (optional)
            sort (str): "Hot", "New", "Old", "Top" (optional)
            unread_only (bool): True to only get unread replies, False
                otherwise (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/user/replies",
                           self._headers, None, params=form)

    def get_report_count(self, community_id: int = None) -> requests.Response:
        """ get_report_count: number of reports

        Args:
            community_id (int): ID of community to query (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/user/report_count",
                           self._headers, None, params=form)

    def get_site(self) -> requests.Response:
        """ get_site: return site info

        Args:
            None

        Returns:
            requests.Response: result of API call
        """

        form = {"auth": self.key}
        return get_handler(f"{self._api_url}/site", self._headers,
                           None, params=form)

    def get_site_metadata(self, url: str) -> requests.Response:
        """ get_site_metadata: return an instance's metadata

        Args:
            url (str): Lemmy instance

        Returns:
            requests.Response: result of API call
        """

        form = {"url": url}
        return get_handler(f"{self._api_url}/post/site_metadata",
                           self._headers, None, params=form)

    def get_unread_count(self) -> requests.Response:
        """ get_unread_count: get number of unread notifications

        Args:
            None

        Returns:
            requests.Response: result of API call
        """

        form = {"auth": self.key}
        return get_handler(f"{self._api_url}/user/unread_count",
                           self._headers, None, params=form)

    def get_unread_registration_application_count(self) -> requests.Response:
        """ get_unread_registration_application_count: number of unread
        instance applications

        Args:
            None

        Returns:
            requests.Response: result of API call
        """

        form = {"auth": self.key}
        return get_handler(
            f"{self._api_url}/admin/registration_application/count",
            self._headers, None, params=form
        )

    def leave_admin(self) -> requests.Response:
        """ leave_admin: current user leaves admin group

        Args:
            None

        Returns:
            requests.Response: result of API call
        """

        form = {"auth": self.key}
        return post_handler(f"{self._api_url}/user/leave_admin",
                            self._headers, form)

    def like_comment(self, comment_id: int, score: int) -> requests.Response:
        """ like_comment: like a comment :)

        Args:
            comment_id (int): ID of comment
            score (int): +1, -1, 0

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/like",
                            self._headers, form)

    def like_post(self, post_id: int, score: int) -> requests.Response:
        """ like_post: like a post :)

        Args:
            post_id (int): ID of post
            score (int): +1, -1, 0

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/like", self._headers, form)

    def list_comment_reports(self, community_id: int = None, limit: int = None,
                             page: int = None, unresolved_only: bool = None
                             ) -> requests.Response:
        """ list_comment_reports: return list of comment reports

        Args:
            community_id (int): ID of community to query (optional)
            limit (int): max. num. reports to obtain (optional)
            page (int): page of results to query (optional)
            unresolved_only (bool): True to get only unresolved reports, False
                otherwise (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/comment/report/list",
                           self._headers, None, params=form)

    def list_communities(self, limit: int = None, page: int = None,
                         sort: str = None,
                         type_: str = None) -> requests.Response:
        """ list_communities: return list of communities

        Args:
            limit (int): max. num. communities to obtain (optional)
            page (int): page of results to query (optional)
            sort (str): "Active", "Hot", "MostComments", "New", "NewComments",
                "Old", "TopAll", "TopDay", "TopMonth", "TopWeek",
                "TopYear" (optional)
            type_ (str): "All", "Community", "Local", "Subscribed" (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/community/list",
                           self._headers, None, params=form)

    def list_post_reports(self, community_id: int = None, limit: int = None,
                          page: int = None, unresolved_only: bool = None
                          ) -> requests.Response:
        """ list_post_reports: return a list of post reports

        Args:
            community_id (int): ID of community to query (optional)
            limit (int): max. num. reports to obtain (optional)
            page (int): page of results to query (optional)
            unresolved_only (bool): True to only get unresolved reports, False
                otherwise (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/post/report/list",
                           self._headers, None, params=form)

    def list_private_message_reports(self, limit: int = None, page: int = None,
                                     unresolved_only: bool = None
                                     ) -> requests.Response:
        """ list_private_message_reports: return a list of private message
        reports

        Args:
            limit (int): max. num. reports to obtain (optional)
            page (int): page of results to query (optional)
            unresolved_only (bool): True to get only unresolved reports, False
                otherwise (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/private_message/report/list",
                           self._headers, None, params=form)

    def list_registration_applications(self, limit: int = None,
                                       page: int = None,
                                       unread_only: bool = None
                                       ) -> requests.Response:
        """ list_registration_applications: return a list of registration
        applications

        Args:
            limit (int): max. num. applications to obtain (optional)
            page (int): page of results to query (optional)
            unread_only (bool): True to get only unread applications, False
                otherwise (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(
            f"{self._api_url}/admin/registration_application/list",
            self._headers, None, params=form
        )

    def lock_post(self, locked: bool, post_id: int) -> requests.Response:
        """ lock_post: lock a post

        Args:
            locked (bool): True if post is locked, False otherwise
            post_id (int): ID of post to lock

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/lock", self._headers, form)

    def login(self, username_or_email: str,
              password: str) -> requests.Response:
        """ login: login

        Args:
            username_or_email (str): username or email for login
            password (str): password for login

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        re = post_handler(f"{self._api_url}/user/login", self._headers, form)
        self.key = re.json()["jwt"]
        return re

    def mark_all_as_read(self) -> requests.Response:
        """ mark_all_as_read: mark all notifications as read

        Args:
            None:

        Returns:
            requests.Response: result of API call
        """

        form = {"auth": self.key}
        return post_handler(f"{self._api_url}/user/mark_all_as_read",
                            self._headers, form)

    def mark_comment_reply_as_read(self, comment_reply_id: int,
                                   read: bool) -> requests.Response:
        """ mark_comment_reply_as_read: mark a comment reply as read

        Args:
            comment_reply_id (int): ID of comment
            read (bool): True if comment is read, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/mark_as_read",
                            self._headers, form)

    def mark_person_mention_as_read(self, person_mention_id: int,
                                    read: bool) -> requests.Response:
        """ mark_person_mention_as_read: mark mention as read

        Args:
            person_mention_id (int): ID of persion mentioned
            read (bool): True if mention is read, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/user/mention/mark_as_read",
                            self._headers, form)

    def mark_post_as_read(self, post_id: int, read: bool) -> requests.Response:
        """ mark_post_as_read: mark a post as read

        Args:
            post_id (int): ID of post
            read (bool): True if post is read, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/mark_as_read",
                            self._headers, form)

    def mark_private_message_as_read(self, private_message_id: int,
                                     read: bool) -> requests.Response:
        """ mark_private_message_as_read: mark a private message as read

        Args:
            private_message_id (int): ID of private message
            read (bool): True if read, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/private_message/mark_as_read",
                            self._headers, form)

    def password_change_after_reset(self, password: str, password_verify: str,
                                    token: str) -> requests.Response:
        """ password_change_after_reset: password change using user token

        Args:
            password (str): new password
            password_verify (str): new password
            token (str): user auth token

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        return post_handler(f"{self._api_url}/user/password_change",
                            self._headers, form)

    def password_reset(self, email: str) -> requests.Response:
        """ password_reset: sent a reset form to user's email

        Args:
            email (str): email of user

        Returns:
            requests.Response: result of API call
        """

        form = {"email": email}
        return post_handler(f"{self._api_url}/user/password_reset",
                            self._headers, form)

    def purge_comment(self, comment_id: int,
                      reason: str = None) -> requests.Response:
        """ purge_comment: purge a comment

        Args:
            comment_id (int): ID of comment
            reason (str): reason for purge (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/purge/comment",
                            self._headers, form)

    def purge_community(self, community_id: int,
                        reason: str = None) -> requests.Response:
        """ purge_community: purge a community

        Args:
            community_id (int): ID of community
            reason (str): reason for purge (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/purge/community",
                            self._headers, form)

    def purge_person(self, person_id: int,
                     reason: str = None) -> requests.Response:
        """ purge_person: purge a person

        Args:
            person_id (int): ID of person
            reason (str): reason for purge (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/purge/person",
                            self._headers, form)

    def purge_post(self, post_id: int,
                   reason: str = None) -> requests.Response:
        """ purge_post: purge a post

        Args:
            post_id (int): ID of post
            reason (str): reason for purge (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/admin/purge/post",
                            self._headers, form)

    def register(self, password: str, password_verify: str, show_nsfw: bool,
                 username: str, answer: str = None, captcha_answer: str = None,
                 captcha_uuid: str = None, email: str = None,
                 honeypot: str = None) -> requests.Response:
        """ register: register a new user

        Args:
            password (str): new user password
            password_verify (str): new user password
            show_nsfw (bool): True to show NSFW content, False otherwise
            username (str): new user username
            answer (str): answer to application question (optional)
            captcha_answer (str): answer to application captcha (optional)
            captcha_uuid (str): UUID of captcha (optional)
            email (str): email address for new user (optional)
            honeypot (str): (optional) TODO: figure out what this does!!

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        return post_handler(f"{self._api_url}/user/register",
                            self._headers, form)

    def remove_comment(self, comment_id: int, removed: bool,
                       reason: str = None) -> requests.Response:
        """ remove_comment: remove a comment

        Args:
            comment_id (int): ID of comment
            removed (bool): True if removed, False otherwise
            reason (str): reason for removal (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/comment/remove",
                            self._headers, form)

    def remove_community(self, community_id: int, removed: bool,
                         expires: int = None,
                         reason: str = None) -> requests.Response:
        """ remove_community: remove a community

        Args:
            community_id (int): ID of community
            removed (bool): True if removed, False otherwise
            expires (int): removal expiry time in UNIX seconds (optional)
            reason (str): reason for removal (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/remove",
                            self._headers, form)

    def remove_post(self, post_id: int, removed: bool,
                    reason: str = None) -> requests.Response:
        """ remove_post: remove a post

        Args:
            post_id (int): ID of post
            removed (bool): True if removed, False otherwise
            reason (str): reason for removal (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/post/remove",
                            self._headers, form)

    def resolve_comment_report(self, report_id: int,
                               resolved: bool) -> requests.Response:
        """ resolve_comment_report: resolve a comment report

        Args:
            report_id (int): ID of comment report
            resolved (bool): True if resolved, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/comment/report/resolve",
                           self._headers, form)

    def resolve_object(self, q: str) -> requests.Response:
        """ resolve_object: resolve object

        Args:
            q (str): query to resolve

        Returns:
            requests.Response: result of API call
        """

        form = {"q": q, "auth": self.key}
        return get_handler(f"{self._api_url}/resolve_object",
                           self._headers, None, params=form)

    def resolve_post_report(self, report_id: int,
                            resolved: bool) -> requests.Response:
        """ resolve_post_report: resolve a post report

        Args:
            report_id (int): ID of post report
            resolved (bool): True if resolved, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/post/report/resolve",
                           self._headers, form)

    def resolve_private_message_report(self, report_id: int,
                                       resolved: bool) -> requests.Response:
        """ resolve_private_message_report: resolve a private message report

        Args:
            report_id (int): ID of private message report
            resolved (bool): True if resolved, False otherwise
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/private_message/report/resolve",
                           self._headers, form)

    def save_comment(self, comment_id: int, save: bool) -> requests.Response:
        """ save_comment: save a comment

        Args:
            comment_id (int): ID of comment
            save (bool): True if saved, False otherwise

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/comment/save",
                           self._headers, form)

    def save_post(self, post_id: int, save: bool) -> requests.Response:
        """ save_post: save a post

        Args:
            post_id (int): ID of post
            save (bool): True if saved, False otherwise

        Returns:
            requests.Response: result of API call
        """

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
        """ save_user_settings: update settings/preferences for currently-
        logged-in user

        Args:
            avatar (str): filepath of avatar to upload (optional)
            banner (str): filepath of banner to upload (optional)
            bio (str): biography (optional)
            bot_account (bool): True if bot, False otherwise (optional)
            default_listing_type (str): "All", "Community", "Local",
                "Subscribed" (optional)
            default_sort_type (str): "Active", "Hot", "MostComments", "New",
                "NewComments", "Old", "TopAll", "TopDay", "TopMonth",
                "TopWeek", "TopYear" (optional)
            discussion_languages (List[int]): languages used (optional)
            display_name (str): display name (optional)
            email (str): email address (optional)
            interface_language (str): language for Lemmy UI (optional)
            matrix_user_id (int): matrix user ID (optional)
            send_notifications_to_email (bool): True to send notifications to
                user's email, False otherwise (optional)
            show_avatars (bool): True to show avatars, False
                otherise (optional)
            show_bot_accounts (bool): True to show bot accounts, False
                otherwise (optional)
            show_new_post_notifs (bool): True to show notifications for new
                posts, False otherwise (optional)
            show_nsfw (bool): True to show NSFW content, False
                otherwise (optional)
            show_read_posts (bool): True to show read posts, False
                otherwise (optional)
            show_scores (bool): True to show scores, False otherwise (optional)
            theme (str): user UI theme (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return put_handler(f"{self._api_url}/user/save_user_settings",
                           self._headers, form)

    def search(self, q: str, community_id: int = None,
               community_name: str = None, creator_id: int = None,
               limit: int = None, listing_type: str = None, page: int = None,
               sort: str = None, type_: str = None) -> requests.Response:
        """ search: search the site/instance

        Args:
            q (str): query
            community_id (int): ID of community to search (optional)
            community_name (str): name of community to search (optional)
            creator_id (int): ID of creator/user (optional)
            limit (int): max. num. entries to obtain (optional)
            listing_type (str): "All", "Community", "Local",
                "Subscribed" (optional)
            page (int): page of results to query (optional)
            sort (str): "Active", "Hot", "MostComments", "New", "NewComments",
                "Old", "TopAll", "TopDay", "TopMonth", "TopWeek",
                "TopYear" (optional)
            type_ (str): "All", "Comments", "Communities", "Posts", "Url",
                "Users" (optional)

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return get_handler(f"{self._api_url}/search", self._headers,
                           None, params=form)

    def transfer_community(self, community_id: int,
                           person_id: int) -> requests.Response:
        """ transfer_community: transfer ownership of a community

        Args:
            community_id (int): ID of community
            person_id (int): ID of new community owner

        Returns:
            requests.Response: result of API call
        """

        form = create_form(locals())
        form["auth"] = self.key
        return post_handler(f"{self._api_url}/community/transfer",
                            self._headers, form)

    def verify_email(self, token: str) -> requests.Response:
        """ verify_email: verify user email using token

        Args:
            token (str): user auth token

        Returns:
            requests.Response: result of API call
        """

        form = {"token": token}
        return post_handler(f"{self._api_url}/user/verify_email",
                            self._headers, form)
