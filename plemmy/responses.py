import requests

from .views import AdminPurgeCommentView, AdminPurgeCommunityView,\
    AdminPurgePersonView, AdminPurgePostView, CommentReplyView,\
    CommentReportView, CommentView, CommunityView, CommunityModeratorView,\
    CustomEmojiView, FederatedInstances, ModAddView, ModAddCommunityView,\
    ModBanView, ModBanFromCommunityView, ModFeaturePostView,\
    ModHideCommunityView, ModLockPostView, ModRemoveCommentView,\
    ModRemovePostView, ModTransferCommunityView, PersonMentionView,\
    PersonView, PostReportView, PostView, PrivateMessageReportView,\
    PrivateMessageView, RegistrationApplicationView, SiteView
from .objects import CaptchaResponse, ImageFile, Language, SiteMetadata,\
    Tagline


class AddAdminResponse(object):
    """https://join-lemmy.org/api/interfaces/AddAdminResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.admins = PersonView(response["admins"])


class AddModToCommunityResponse(object):
    """https://join-lemmy.org/api/interfaces/AddModToCommunityResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.moderators = CommunityModeratorView(response["moderators"])


class BanFromCommunityResponse(object):
    """https://join-lemmy.org/api/interfaces/BanFromCommunityResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.banned = response["banned"]
        self.person_view = PersonView(response["person_view"])


class BanPersonResponse(object):
    """https://join-lemmy.org/api/interfaces/BanPersonResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.banned = response["banned"]
        self.person_view = PersonView(response["person_view"])


class BannedPersonsResponse(object):
    """https://join-lemmy.org/api/interfaces/BannedPersonsResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.banned = [PersonView(p) for p in response["banned"]]


class BlockCommunityResponse(object):
    """https://join-lemmy.org/api/interfaces/BlockCommunityResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.blocked = response["blocked"]
        self.community_view = CommunityView(response["community_view"])


class BlockPersonResponse(object):
    """https://join-lemmy.org/api/interfaces/BlockPersonResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.blocked = response["blocked"]
        self.person_view = PersonView(response["person_view"])


class CommentReplyResponse(object):
    """https://join-lemmy.org/api/interfaces/CommentReplyResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.comment_reply_view = CommentReplyView(
            response["comment_reply_view"]
        )


class CommentReportResponse(object):
    """https://join-lemmy.org/api/interfaces/CommentReportResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.comment_report_view = CommentReportView(
            response["comment_report_view"]
        )


class CommentResponse(object):
    """https://join-lemmy.org/api/interfaces/CommentResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.comment_view = CommentView(response["comment_view"])
        if "form_id" in response.keys():
            self.form_id = response["form_id"]
        else:
            self.form_id = None
        self.recipient_ids = response["recipient_ids"]


class CommunityResponse(object):
    """https://join-lemmy.org/api/interfaces/CommunityResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.community_view = CommunityView(response["community_view"])
        self.discussion_languages = response["discussion_languages"]


class CustomEmojiResponse(object):
    """https://join-lemmy.org/api/interfaces/CustomEmojiResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.custom_emoji = CustomEmojiView(response["custom_emoji"])


class DeleteCustomEmojiResponse(object):
    """https://join-lemmy.org/api/interfaces/DeleteCustomEmojiResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.id = response["id"]
        self.success = response["success"]


class GetCaptchaResponse(object):
    """https://join-lemmy.org/api/interfaces/GetCaptchaResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        if "ok" in response.keys():
            self.ok = CaptchaResponse(**response["ok"])
        else:
            self.ok = None


class GetCommentsResponse(object):
    """https://join-lemmy.org/api/interfaces/GetCommentsResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.comments = [CommentView(c) for c in response["comments"]]


class GetCommunityResponse(object):
    """https://join-lemmy.org/api/interfaces/GetCommunityResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.community_view = CommunityView(response["community_view"])
        self.discussion_languages = response["discussion_languages"]
        self.moderators = [CommunityModeratorView(m)
                           for m in response["moderators"]]


class GetFederatedInstancesResponse(object):
    """https://join-lemmy.org/api/interfaces/GetFederatedInstancesResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        if "federated_instances" in response.keys():
            self.federated_instances = FederatedInstances(
                response["federated_instances"]
            )
        else:
            self.federated_instances = None


class GetModlogResponse(object):
    """https://join-lemmy.org/api/interfaces/GetModlogResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.added = ModAddView(response["added"])
        self.added_to_community = ModAddCommunityView(
            response["added_to_community"]
        )
        self.admin_purged_comments = AdminPurgeCommentView(
            response["admin_purged_comments"]
        )
        self.admin_purged_communities = AdminPurgeCommunityView(
            response["admin_purged_communities"]
        )
        self.admin_purged_persons = AdminPurgePersonView(
            response["admin_purged_persons"]
        )
        self.admin_purged_posts = AdminPurgePostView(
            response["admin_purged_posts"]
        )
        self.banned = ModBanView(response["banned"])
        self.banned_from_community = ModBanFromCommunityView(
            response["banned_from_community"]
        )
        self.featured_posts = ModFeaturePostView(response["featured_posts"])
        self.hidden_communities = ModHideCommunityView(
            response["hidden_communities"]
        )
        self.locked_posts = ModLockPostView(response["locked_posts"])
        self.removed_comments = ModRemoveCommentView(
            response["removed_comments"]
        )
        self.removed_posts = ModRemovePostView(response["removed_posts"])
        self.transferred_to_community = ModTransferCommunityView(
            response["transferred_to_community"]
        )


class GetPersonDetailsResponse(object):
    """https://join-lemmy.org/api/interfaces/GetPersonDetailsResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.comments = CommentView(response["comments"])
        self.moderates = CommunityModeratorView(response["moderates"])
        self.person_view = PersonView(response["person_view"])
        self.posts = [PostView(p) for p in response["posts"]]


class GetPersonMentionsResponse(object):
    """https://join-lemmy.org/api/interfaces/GetPersonMentionsResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.mentions = PersonMentionView(response["mentions"])


class GetPostResponse(object):
    """https://join-lemmy.org/api/interfaces/GetPostResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.community_view = CommunityView(response["community_view"])
        self.cross_posts = [PostView(p) for p in response["cross_posts"]]
        self.moderators = [CommunityModeratorView(m) for m in response["moderators"]]
        self.post_view = PostView(response["post_view"])


class GetPostsResponse(object):
    """https://join-lemmy.org/api/interfaces/GetPostsResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.posts = [PostView(p) for p in response["posts"]]


class GetRepliesResponse(object):
    """https://join-lemmy.org/api/interfaces/GetRepliesResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.replies = CommentReplyView(response["replies"])


class GetReportCountResponse(object):
    """https://join-lemmy.org/api/interfaces/GetReportCountResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.comment_reports = response["comment_reports"]
        if "community_id" in response.keys():
            self.community_id = response["communtiy_id"]
        else:
            self.community_id = None
        self.post_reports = response["post_reports"]
        if "private_message_reports" in response.keys():
            self.private_message_reports = response["private_message_reports"]
        else:
            self.private_message_reports = None


class GetSiteMetadataResponse(object):
    """https://join-lemmy.org/api/interfaces/GetSiteMetadataResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.metadata = SiteMetadata(**response["metadata"])


class GetSiteResponse(object):
    """https://join-lemmy.org/api/interfaces/GetSiteResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.admins = [PersonView(a) for a in response["admins"]]
        self.all_languages = [Language(**lang)
                              for lang in response["all_languages"]]
        self.discussion_languages = response["discussion_languages"]
        if "my_user" in response.keys():
            self.my_user = response["my_user"]
        else:
            self.my_user = None
        self.site_view = SiteView(response["site_view"])
        self.taglines = [Tagline(**t) for t in response["taglines"]]
        self.version = response["version"]


class GetUnreadCountResponse(object):
    """https://join-lemmy.org/api/interfaces/GetUnreadCountResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.mentions = response["mentions"]
        self.private_messages = response["private_messages"]
        self.replies = response["replies"]


class GetUnreadRegistrationApplicationCountResponse(object):
    """https://join-lemmy.org/api/interfaces/GetUnreadRegistrationApplicationCountResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.registration_applications = response["registration_applications"]


class ListCommentReportsResponse(object):
    """https://join-lemmy.org/api/interfaces/ListCommentReportsResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.comment_reports = [CommentReportView(v)
                                for v in response["comment_reports"]]


class ListCommunitiesResponse(object):
    """https://join-lemmy.org/api/interfaces/ListCommunitiesResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.communities = [CommunityView(c) for c in response["communities"]]


class ListPostReportsResponse(object):
    """https://join-lemmy.org/api/interfaces/ListPostReportsResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.post_reports = [PostReportView(r)
                             for r in response["post_reports"]]


class ListPrivateMessageReportsResponse(object):
    """https://join-lemmy.org/api/interfaces/ListPrivateMessageReportsResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.private_message_reports = [PrivateMessageReportView(r)
                                        for r in response[
                                            "private_message_reports"
                                        ]]


class ListRegistrationApplicationsResponse(object):
    """https://join-lemmy.org/api/interfaces/ListRegistrationApplicationsResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.registration_applications = [RegistrationApplicationView(a)
                                          for a in response[
                                              "registration_applications"
                                          ]]


class LoginResponse(object):
    """https://join-lemmy.org/api/interfaces/LoginResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        if "jwt" in response.keys():
            self.jwt = response["jwt"]
        else:
            self.jwt = None
        self.registration_created = response["registration_created"]
        self.verify_email_sent = response["verify_email_sent"]


class PersonMentionResponse(object):
    """https://join-lemmy.org/api/interfaces/PersonMentionResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.person_mention_view = PersonMentionView(
            response["person_mention_view"]
        )


class PostReportResponse(object):
    """https://join-lemmy.org/api/interfaces/PostReportResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.post_report_view = PostReportView(response["post_report_view"])


class PostResponse(object):
    """https://join-lemmy.org/api/interfaces/PostResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.post_view = PostView(response["post_view"])


class PrivateMessageReportResponse(object):
    """https://join-lemmy.org/api/interfaces/PrivateMessageReportResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.private_message_report_view = PrivateMessageReportView(
            response["private_message_report_view"]
        )


class PrivateMessageResponse(object):
    """https://join-lemmy.org/api/interfaces/PrivateMessageResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.private_message_view = PrivateMessageView(
            response["private_message_view"]
        )


class PurgeItemResponse(object):
    """https://join-lemmy.org/api/interfaces/PurgeItemResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.success = response["success"]


class RegistrationApplicationResponse(object):
    """https://join-lemmy.org/api/interfaces/RegistrationApplicationResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.registration_application = RegistrationApplicationView(
            response["registration_application"]
        )


class ResolveObjectResponse(object):
    """https://join-lemmy.org/api/interfaces/ResolveObjectResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        if "comment" in response.keys():
            self.comment = CommentView(response["comment"])
        else:
            self.comment = None
        if "community" in response.keys():
            self.community = CommunityView(response["community"])
        else:
            self.community = None
        if "person" in response.keys():
            self.person = PersonView(response["person"])
        else:
            self.person = None
        if "post" in response.keys():
            self.post = PostView(response["post"])
        else:
            self.post = None


class SearchResponse(object):
    """https://join-lemmy.org/api/interfaces/SearchResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.comments = [CommentView(c) for c in response["comments"]]
        self.communities = [CommunityView(c) for c in response["communities"]]
        self.posts = [PostView(p) for p in response["posts"]]
        self.type_ = response["type_"]
        self.users = [PersonView(p) for p in response["users"]]


class SiteResponse(object):
    """https://join-lemmy.org/api/interfaces/SiteResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        self.site_view = SiteView(response["site_view"])
        self.taglines = [Tagline(**t) for t in response["taglines"]]


class UploadImageResponse(object):
    """https://join-lemmy.org/api/interfaces/UploadImageResponse.html"""

    def __init__(self, api_response: requests.Response) -> None:

        response = api_response.json()
        if "delete_url" in response.keys():
            self.delete_url = response["delete_url"]
        else:
            self.delete_url = None
        if "files" in response.keys():
            self.files = [ImageFile(**f) for f in response["files"]]
        self.msg = response["msg"]
        if "url" in response.keys():
            self.url = response["url"]
        else:
            self.url = None
