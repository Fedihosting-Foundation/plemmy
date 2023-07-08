from .objects import AdminPurgeComment, AdminPurgeCommunity,\
    AdminPurgePerson, AdminPurgePost, Comment, CommentAggregates,\
    CommentReply, CommentReport, Community, CommunityAggregates, CustomEmoji,\
    CustomEmojiKeyword, Instance, LocalSite, LocalSiteRateLimit, LocalUser,\
    ModAdd, ModAddCommunity, ModBan, ModBanFromCommunity, ModFeaturePost,\
    ModHideCommunity, ModLockPost, ModRemoveComment, ModRemoveCommunity,\
    ModRemovePost, ModTransferCommunity, Person, PersonAggregates,\
    PersonMention, Post, PostAggregates, PostReport, PrivateMessage,\
    PrivateMessageReport, RegistrationApplication, Site, SiteAggregates


class ViewObject(object):
    """ ViewObject: parent object to all view-related objects """

    def __init__(self, view: dict) -> None:

        self._view = view
        self.parse()

    def parse(self) -> None:

        return


class AdminPurgeCommentView(ViewObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgeCommentView.html"""

    def parse(self) -> None:

        if "admin" in self._view.keys():
            self.admin = Person(**self._view["admin"])
        else:
            self.admin = None
        self.admin_purge_comment = AdminPurgeComment(
            **self._view["admin_purge_comment"]
        )
        self.post = Post(**self._view["post"])


class AdminPurgeCommunityView(ViewObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgeCommunityView.html"""

    def parse(self) -> None:

        if "admin" in self._view.keys():
            self.admin = Person(**self._view["admin"])
        else:
            self.admin = None
        self.admin_purge_community = AdminPurgeCommunity(
            **self._view["admin_purge_community"]
        )


class AdminPurgePersonView(ViewObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgePersonView.html"""

    def parse(self) -> None:

        if "admin" in self._view.keys():
            self.admin = Person(**self._view["admin"])
        else:
            self.admin = None
        self.admin_purge_person = AdminPurgePerson(
            **self._view["admin_purge_person"]
        )


class AdminPurgePostView(ViewObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgePostView.html"""

    def parse(self) -> None:

        if "admin" in self._view.keys():
            self.admin = Person(**self._view["admin"])
        self.admin_purge_post = AdminPurgePost(
            **self._view["admin_purge_post"]
        )
        self.community = Community(**self._view["community"])


class CommentReplyView(ViewObject):
    """https://join-lemmy.org/api/interfaces/CommentReplyView.html"""

    def parse(self) -> None:

        self.comment = Comment(**self._view["comment"])
        self.comment_reply = CommentReply(**self._view["comment_reply"])
        self.community = Community(**self._view["community"])
        self.counts = CommentAggregates(**self._view["counts"])
        self.creator = Person(**self._view["creator"])
        self.creator_banned_from_community = self._view[
            "creator_banned_from_community"
        ]
        self.creator_blocked = self._view["creator_blocked"]
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None
        self.post = Post(**self._view["post"])
        self.recipient = Person(**self._view["recipient"])
        self.saved = self._view["saved"]
        self.subscribed = self._view["subscribed"]


class CommentReportView(ViewObject):
    """https://join-lemmy.org/api/interfaces/CommentReportView.html"""

    def parse(self) -> None:

        self.comment = Comment(**self._view["comment"])
        self.comment_creator = Person(**self._view["comment_creator"])
        self.comment_report = CommentReport(**self._view["comment_report"])
        self.community = Community(**self._view["community"])
        self.counts = CommentAggregates(**self._view["counts"])
        self.creator = Person(**self._view["creator"])
        self.creator_banned_from_community = self._view[
            "creator_banned_from_community"
        ]
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None
        self.post = Post(**self._view["post"])
        if "resolver" in self._view.keys():
            self.resolver = Person(**self._view["resolver"])
        else:
            self.resolver = None


class CommentView(ViewObject):
    """https://join-lemmy.org/api/interfaces/CommentView.html"""

    def parse(self) -> None:

        self.comment = Comment(**self._view["comment"])
        self.community = Community(**self._view["community"])
        self.counts = CommentAggregates(**self._view["counts"])
        self.creator = Person(**self._view["creator"])
        self.creator_banned_from_community = self._view[
            "creator_banned_from_community"
        ]
        self.creator_blocked = self._view["creator_blocked"]
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None
        self.post = Post(**self._view["post"])
        self.saved = self._view["saved"]
        self.subscribed = self._view["subscribed"]


class CommunityModeratorView(ViewObject):
    """https://join-lemmy.org/api/interfaces/CommunityModeratorView.html"""

    def parse(self) -> None:

        self.community = Community(**self._view["community"])
        self.moderator = Person(**self._view["moderator"])


class CommunityView(ViewObject):
    """https://join-lemmy.org/api/interfaces/CommunityView.html"""

    def parse(self) -> None:

        self.blocked = self._view["blocked"]
        self.community = Community(**self._view["community"])
        self.counts = CommunityAggregates(**self._view["counts"])
        self.subscribed = self._view["subscribed"]


class CustomEmojiView(ViewObject):
    """https://join-lemmy.org/api/interfaces/CustomEmojiView.html"""

    def parse(self) -> None:

        self.custom_emoji = CustomEmoji(**self._view["custom_emoji"])
        self.keywords = CustomEmojiKeyword(**self._view["keywords"])


class FederatedInstances(ViewObject):
    """https://join-lemmy.org/api/interfaces/FederatedInstances.html"""

    def parse(self) -> None:

        self.allowed = [Instance(**i) for i in self._view["allowed"]]
        self.blocked = [Instance(**i) for i in self._view["blocked"]]
        self.linked = [Instance(**i) for i in self._view["linked"]]


class ModAddCommunityView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModAddCommunityView.html"""

    def parse(self) -> None:

        self.community = Community(**self._view["community"])
        self.mod_add_community = ModAddCommunity(
            **self._view["mod_add_community"]
        )
        self.modded_person = Person(**self._view["modded_person"])
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None


class ModAddView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModAddView.html"""

    def parse(self) -> None:

        self.mod_add = ModAdd(**self._view["mod_add"])
        self.modded_person = Person(**self._view["modded_person"])
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None


class ModBanFromCommunityView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModBanFromCommunityView.html"""

    def parse(self) -> None:

        self.banned_person = Person(**self._view["banned_person"])
        self.community = Community(**self._view["community"])
        self.mod_ban_from_community = ModBanFromCommunity(
            **self._view["mod_ban_from_community"]
        )
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None


class ModBanView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModBanView.html"""

    def parse(self) -> None:

        self.banned_person = Person(**self._view["banned_person"])
        self.mod_ban = ModBan(**self._view["mod_ban"])
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None


class ModFeaturePostView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModFeaturePostView.html"""

    def parse(self) -> None:

        self.community = Community(**self._view["community"])
        self.mod_feature_post = ModFeaturePost(
            **self._view["mod_feature_post"]
        )
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None
        self.post = Post(**self._view["post"])


class ModHideCommunityView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModHideCommunityView.html"""

    def parse(self) -> None:

        if "admin" in self._view.keys():
            self.admin = Person(**self._view["admin"])
        else:
            self.admin = None
        self.community = Community(**self._view["community"])
        self.mod_hide_community = ModHideCommunity(
            **self._view["mod_hide_community"]
        )


class ModLockPostView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModLockPostView.html"""

    def parse(self) -> None:

        self.community = Community(**self._view["community"])
        self.mod_lock_post = ModLockPost(**self._view["mod_lock_post"])
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None
        self.post = Post(**self._view["post"])


class ModRemoveCommentView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModRemoveCommentView.html"""

    def parse(self) -> None:

        self.comment = Comment(**self._view["comment"])
        self.commenter = Person(**self._view["commenter"])
        self.community = Community(**self._view["community"])
        self.mod_remove_comment = ModRemoveComment(
            **self._view["mod_remove_comment"]
        )
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None
        self.post = Post(**self._view["post"])


class ModRemoveCommunityView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModRemoveCommunityView.html"""

    def parse(self) -> None:

        self.community = Community(**self._view["community"])
        self.mod_remove_community = ModRemoveCommunity(
            **self._view["mod_remove_community"]
        )
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None


class ModRemovePostView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModRemovePostView.html"""

    def parse(self) -> None:

        self.community = Community(**self._view["community"])
        self.mod_remove_post = ModRemovePost(**self._view["mod_remove_post"])
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None
        self.post = Post(**self._view["post"])


class ModTransferCommunityView(ViewObject):
    """https://join-lemmy.org/api/interfaces/ModTransferCommunityView.html"""

    def parse(self) -> None:

        self.community = Community(**self._view["community"])
        self.mod_transfer_community = ModTransferCommunity(
            **self._view["mod_transfer_community"]
        )
        self.modded_person = Person(**self._view["modded_person"])
        if "moderator" in self._view.keys():
            self.moderator = Person(**self._view["moderator"])
        else:
            self.moderator = None


class PersonMentionView(ViewObject):
    """https://join-lemmy.org/api/interfaces/PersonMentionView.html"""

    def parse(self) -> None:

        self.comment = Comment(**self._view["comment"])
        self.community = Community(**self._view["community"])
        self.counts = CommentAggregates(**self._view["counts"])
        self.creator = Person(**self._view["creator"])
        self.creator_banned_from_community = self._view[
            "creator_banned_from_community"
        ]
        self.creator_blocked = self._view["creator_blocked"]
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None
        self.person_mention = PersonMention(**self._view["person_mention"])
        self.post = Post(**self._view["post"])
        self.recipient = Person(**self._view["recipient"])
        self.saved = self._view["saved"]
        self.subscribed = self._view["subscribed"]


class PersonView(ViewObject):
    """https://join-lemmy.org/api/interfaces/PersonView.html"""

    def parse(self) -> None:

        self.counts = PersonAggregates(**self._view["counts"])
        self.person = Person(**self._view["person"])


class PostReportView(ViewObject):
    """https://join-lemmy.org/api/interfaces/PostReportView.html"""

    def parse(self) -> None:

        self.community = Community(**self._view["community"])
        self.counts = PostAggregates(**self._view["counts"])
        self.creator = Person(**self._view["creator"])
        self.creator_banned_from_community = self._view[
            "creator_banned_from_community"
        ]
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None
        self.post = Post(**self._view["post"])
        self.post_creator = Person(**self._view["post_creator"])
        self.post_report = PostReport(**self._view["post_report"])
        if "resolver" in self._view.keys():
            self.resolver = Person(**self._view["resolver"])
        else:
            self.resolver = None


class PostView(ViewObject):
    """https://join-lemmy.org/api/interfaces/PostView.html"""

    def parse(self) -> None:

        self.community = Community(**self._view["community"])
        self.counts = PostAggregates(**self._view["counts"])
        self.creator = Person(**self._view["creator"])
        self.creator_banned_from_community = self._view[
            "creator_banned_from_community"
        ]
        self.creator_blocked = self._view["creator_blocked"]
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None
        self.post = Post(**self._view["post"])
        self.read = self._view["read"]
        self.saved = self._view["saved"]
        self.subscribed = self._view["subscribed"]
        self.unread_comments = self._view["unread_comments"]


class PrivateMessageReportView(ViewObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessageReportView.html"""

    def parse(self) -> None:

        self.creator = Person(**self._view["creator"])
        self.private_message = PrivateMessage(**self._view["private_message"])
        self.private_message_creator = Person(
            **self._view["private_message_creator"]
        )
        self.private_message_report = PrivateMessageReport(
            **self._view["private_message_report"]
        )
        if "resolver" in self._view.keys():
            self.resolver = Person(**self._view["resolver"])
        else:
            self.resolver = None


class PrivateMessageView(ViewObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessageView.html"""

    def parse(self) -> None:

        self.creator = Person(**self._view["creator"])
        self.private_message = PrivateMessage(**self._view["private_message"])
        self.recipient = Person(**self._view["recipient"])


class RegistrationApplicationView(ViewObject):
    """https://join-lemmy.org/api/interfaces/RegistrationApplicationView.html"""

    def parse(self) -> None:

        if "admin" in self._view.keys():
            self.admin = Person(**self._view["admin"])
        else:
            self.admin = None
        self.creator = Person(**self._view["creator"])
        self.creator_local_user = LocalUser(**self._view["creator_local_user"])
        self.registration_application = RegistrationApplication(
            **self._view["registration_application"]
        )


class SiteView(ViewObject):
    """https://join-lemmy.org/api/interfaces/SiteView.html"""

    def parse(self) -> None:

        self.counts = SiteAggregates(**self._view["counts"])
        self.local_site = LocalSite(**self._view["local_site"])
        self.local_site_rate_limit = LocalSiteRateLimit(
            **self._view["local_site_rate_limit"]
        )
        self.site = Site(**self._view["site"])
