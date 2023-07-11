from dataclasses import dataclass


@dataclass
class AdminPurgeComment:
    """https://join-lemmy.org/api/interfaces/AdminPurgeComment.html"""

    admin_person_id: int = None
    id: int = None
    post_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class AdminPurgeCommunity:
    """https://join-lemmy.org/api/interfaces/AdminPurgeCommunity.html"""

    admin_person_id: int = None
    id: int = None
    reason: str = None
    when_: str = None


@dataclass
class AdminPurgePerson:
    """https://join-lemmy.org/api/interfaces/AdminPurgePerson.html"""

    admin_person_id: int = None
    id: int = None
    reason: str = None
    when_: str = None


@dataclass
class AdminPurgePost:
    """https://join-lemmy.org/api/interfaces/AdminPurgePost.html"""

    admin_person_id: int = None
    community_id: int = None
    id: int = None
    reason: str = None
    when_: str = None


@dataclass
class CaptchaResponse:
    """https://join-lemmy.org/api/interfaces/CaptchaResponse.html"""

    png: str = None
    uuid: str = None
    wav: str = None


@dataclass
class Comment:
    """https://join-lemmy.org/api/interfaces/Comment.html"""

    ap_id: str = None
    content: str = None
    creator_id: int = None
    deleted: bool = None
    distinguished: bool = None
    id: int = None
    language_id: int = None
    local: bool = None
    path: str = None
    post_id: int = None
    published: str = None
    removed: bool = None
    updated: str = None


@dataclass
class CommentAggregates:
    """https://join-lemmy.org/api/interfaces/CommentAggregates.html"""

    child_count: int = None
    comment_id: int = None
    downvotes: int = None
    hot_rank: int = None
    id: int = None
    published: str = None
    score: int = None
    upvotes: int = None


@dataclass
class CommentReply:
    """https://join-lemmy.org/api/interfaces/CommentReply.html"""

    comment_id: int = None
    id: int = None
    published: str = None
    read: bool = None
    recipient_id: int = None


@dataclass
class CommentReport:
    """https://join-lemmy.org/api/interfaces/CommentReport.html"""

    comment_id: int = None
    creator_id: int = None
    id: int = None
    original_comment_text: str = None
    published: str = None
    reason: str = None
    resolved: bool = None
    resolver_id: int = None
    updated: str = None


@dataclass
class Community:
    """https://join-lemmy.org/api/interfaces/Community.html"""

    description: str = None
    icon: str = None
    id: int = None
    name: str = None
    title: str = None
    removed: bool = None
    published: str = None
    deleted: bool = None
    nsfw: bool = None
    actor_id: str = None
    local: bool = None
    hidden: bool = None
    posting_restricted_to_mods: bool = None
    instance_id: int = None
    updated: str = None
    banner: bool = None


@dataclass
class CommunityAggregates:
    """https://join-lemmy.org/api/interfaces/CommunityAggregates.html"""

    id: int = None
    community_id: int = None
    subscribers: int = None
    posts: int = None
    comments: int = None
    published: str = None
    users_active_day: int = None
    users_active_week: int = None
    users_active_month: int = None
    users_active_half_year: int = None
    hot_rank: int = None


@dataclass
class CustomEmoji:
    """https://join-lemmy.org/api/interfaces/CustomEmoji.html"""

    alt_text: str = None
    category: str = None
    id: int = None
    image_url: str = None
    local_site_id: int = None
    published: str = None
    shortcode: str = None
    updated: str = None


@dataclass
class CustomEmojiKeyword:
    """https://join-lemmy.org/api/interfaces/CustomEmojiKeyword.html"""

    custom_emoji_id: int = None
    id: int = None
    keyword: str = None


@dataclass
class ImageFile:
    """https://join-lemmy.org/api/interfaces/ImageFile.html"""

    delete_token: str = None
    file: str = None


@dataclass
class Instance:
    """https://join-lemmy.org/api/interfaces/Instance.html"""

    domain: str = None
    id: int = None
    published: str = None
    software: str = None
    updated: str = None
    version: str = None


@dataclass
class Language:
    """https://join-lemmy.org/api/interfaces/Language.html"""

    code: str = None
    id: int = None
    name: str = None


@dataclass
class LocalSite:
    """https://join-lemmy.org/api/interfaces/LocalSite.html"""

    actor_name_max_length: int = None
    application_email_admins: bool = None
    application_question: str = None
    captcha_difficulty: str = None
    captcha_enabled: bool = None
    community_creation_admin_only: bool = None
    default_post_listing_type: str = None
    default_theme: str = None
    enable_downvotes: bool = None
    enable_nsfw: bool = None
    federation_enabled: bool = None
    hide_modlog_mod_names: bool = None
    id: int = None
    legal_information: str = None
    private_instance: bool = None
    published: str = None
    registration_mode: str = None
    reports_email_admins: bool = None
    require_email_verification: bool = None
    site_id: int = None
    site_setup: bool = None
    slur_filter_regex: str = None
    updated: str = None


@dataclass
class LocalSiteRateLimit:
    """https://join-lemmy.org/api/interfaces/LocalSiteRateLimit.html"""

    comment: int = None
    comment_per_second: int = None
    id: int = None
    image: int = None
    image_per_second: int = None
    local_site_id: int = None
    message: int = None
    message_per_second: int = None
    post: int = None
    post_per_second: int = None
    published: str = None
    register: int = None
    register_per_second: int = None
    search: int = None
    search_per_second: int = None
    updated: str = None


@dataclass
class LocalUser:
    """https://join-lemmy.org/api/interfaces/LocalUser.html"""

    accepted_application: bool = None
    default_listing_type: str = None
    default_sort_type: str = None
    email: str = None
    email_verified: bool = None
    id: int = None
    interface_language: str = None
    open_links_in_new_tab: bool = None
    person_id: int = None
    send_notifications_to_email: bool = None
    show_avatars: bool = None
    show_bot_accounts: bool = None
    show_new_post_notifs: bool = None
    show_nsfw: bool = None
    show_read_posts: bool = None
    show_scores: bool = None
    theme: str = None
    totp_2fa_url: str = None
    validator_time: str = None


@dataclass
class ModAdd:
    """https://join-lemmy.org/api/interfaces/ModAdd.html"""

    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    removed: bool = None
    when_: str = None


@dataclass
class ModAddCommunity:
    """https://join-lemmy.org/api/interfaces/ModAddCommunity.html"""

    community_id: int = None
    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    removed: bool = None
    when_: str = None


@dataclass
class ModBan:
    """https://join-lemmy.org/api/interfaces/ModBan.html"""

    banned: bool = None
    expires: str = None
    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class ModBanFromCommunity:
    """https://join-lemmy.org/api/interfaces/ModBanFromCommunity.html"""

    banned: bool = None
    community_id: int = None
    expires: str = None
    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class ModFeaturePost:
    """https://join-lemmy.org/api/interfaces/ModFeaturePost.html"""

    featured: bool = None
    id: int = None
    is_featured_community: bool = None
    mod_person_id: int = None
    post_id: int = None
    when_: str = None


@dataclass
class ModHideCommunity:
    """https://join-lemmy.org/api/interfaces/ModHideCommunity.html"""

    community_id: int = None
    hidden: bool = None
    id: int = None
    mod_person_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class ModLockPost:
    """https://join-lemmy.org/api/interfaces/ModLockPost.html"""

    id: int = None
    locked: bool = None
    mod_person_id: int = None
    post_id: int = None
    when_: str = None


@dataclass
class ModRemoveComment:
    """https://join-lemmy.org/api/interfaces/ModRemoveComment.html"""

    comment_id: int = None
    id: int = None
    mod_person_id: int = None
    removed: bool = None
    reason: str = None
    when_: str = None


@dataclass
class ModRemoveCommunity:
    """https://join-lemmy.org/api/interfaces/ModRemoveCommunity.html"""

    community_id: int = None
    expires: str = None
    id: int = None
    mod_person_id: int = None
    removed: bool = None
    reason: str = None
    when_: str = None


@dataclass
class ModRemovePost:
    """https://join-lemmy.org/api/interfaces/ModRemovePost.html"""

    id: int = None
    mod_person_id: int = None
    post_id: int = None
    removed: bool = None
    reason: str = None
    when_: str = None


@dataclass
class ModTransferCommunity:
    """https://join-lemmy.org/api/interfaces/ModTransferCommunity.html"""

    community_id: int = None
    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    when_: str = None


@dataclass
class Person:
    """https://join-lemmy.org/api/interfaces/Person.html"""

    actor_id: str = None
    admin: bool = None
    avatar: str = None
    ban_expires: str = None
    banned: bool = None
    banner: str = None
    bio: str = None
    bot_account: bool = None
    deleted: bool = None
    display_name: str = None
    id: int = None
    inbox_url: str = None
    instance_id: int = None
    local: bool = None
    matrix_user_id: str = None
    name: str = None
    published: str = None
    updated: str = None


@dataclass
class PersonAggregates:
    """https://join-lemmy.org/api/interfaces/PersonAggregates.html"""

    comment_count: int = None
    comment_score: int = None
    id: int = None
    person_id: int = None
    post_count: int = None
    post_score: int = None


@dataclass
class PersonMention:
    """https://join-lemmy.org/api/interfaces/PersonMention.html"""

    comment_id: int = None
    id: int = None
    published: str = None
    read: bool = None
    recipient_id: int = None


@dataclass
class Post:
    """https://join-lemmy.org/api/interfaces/Post.html"""

    ap_id: str = None
    body: str = None
    community_id: int = None
    creator_id: int = None
    deleted: bool = None
    embed_description: str = None
    embed_title: str = None
    embed_video_url: str = None
    featured_community: bool = None
    featured_local: bool = None
    id: int = None
    language_id: int = None
    local: bool = None
    locked: bool = None
    name: str = None
    nsfw: bool = None
    published: str = None
    removed: bool = None
    thumbnail_url: str = None
    updated: str = None
    url: str = None


@dataclass
class PostAggregates:
    """https://join-lemmy.org/api/interfaces/PostAggregates.html"""

    comments: int = None
    downvotes: int = None
    featured_community: bool = None
    featured_local: bool = None
    hot_rank: int = None
    hot_rank_active: int = None
    id: int = None
    newest_comment_time: str = None
    newest_comment_time_necro: str = None
    post_id: int = None
    published: str = None
    score: int = None
    upvotes: int = None


@dataclass
class PostReport:
    """https://join-lemmy.org/api/interfaces/PostReport.html"""

    creator_id: int = None
    id: int = None
    original_post_body: str = None
    original_post_name: str = None
    original_post_url: str = None
    post_id: int = None
    published: str = None
    reason: str = None
    resolved: bool = None
    resolver_id: int = None
    updated: str = None


@dataclass
class PrivateMessage:
    """https://join-lemmy.org/api/interfaces/PrivateMessage.html"""

    ap_id: str = None
    content: str = None
    creator_id: int = None
    deleted: bool = None
    id: int = None
    local: bool = None
    published: str = None
    read: bool = None
    recipient_id: int = None
    updated: str = None


@dataclass
class PrivateMessageReport:
    """https://join-lemmy.org/api/interfaces/PrivateMessageReport.html"""

    creator_id: int = None
    id: int = None
    original_pm_text: str = None
    private_message_id: int = None
    published: str = None
    reason: str = None
    resolved: bool = None
    resolver_id: int = None
    updated: str = None


@dataclass
class RegistrationApplication:
    """https://join-lemmy.org/api/interfaces/RegistrationApplication.html"""

    admin_id: int = None
    answer: str = None
    deny_reason: str = None
    id: int = None
    local_user_id: int = None
    published: str = None


@dataclass
class Site:
    """https://join-lemmy.org/api/interfaces/Site.html"""

    actor_id: str = None
    banner: str = None
    description: str = None
    icon: str = None
    id: int = None
    inbox_url: str = None
    instance_id: int = None
    last_refreshed_at: str = None
    name: str = None
    private_key: str = None
    public_key: str = None
    published: str = None
    sidebar: str = None
    updated: str = None


@dataclass
class SiteAggregates:
    """https://join-lemmy.org/api/interfaces/SiteAggregates.html"""

    comments: int = None
    communities: int = None
    id: int = None
    posts: int = None
    site_id: int = None
    users: int = None
    users_active_day: int = None
    users_active_half_year: int = None
    users_active_month: int = None
    users_active_week: int = None


@dataclass
class SiteMetadata:
    """https://join-lemmy.org/api/interfaces/SiteMetadata.html"""

    description: str = None
    embed_video_url: str = None
    image: str = None
    title: str = None


@dataclass
class Tagline:
    """https://join-lemmy.org/api/interfaces/Tagline.html"""

    content: str = None
    id: int = None
    local_site_id: int = None
    published: str = None
    updated: str = None
