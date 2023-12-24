from datetime import datetime
import os
import pytest

import plemmy
from plemmy.responses import PostResponse


COMMUNITY_ID: int = int(os.environ.get("COMMUNITY_ID"))
COMMUNITY_NAME: str = os.environ.get("COMMUNITY_NAME")
INSTANCE_URL: str = os.environ.get("INSTANCE_URL")
PASSWORD: str = os.environ.get("PASSWORD")
USERNAME: str = os.environ.get("USERNAME")


def test_login() -> None:

    instance = plemmy.LemmyHttp(INSTANCE_URL)
    response = instance.login(USERNAME, PASSWORD)
    if response.status_code != 200:
        pytest.fail(f"{response.reason}")


def test_get_community() -> None:

    instance = plemmy.LemmyHttp(INSTANCE_URL)
    instance.login(USERNAME, PASSWORD)
    response = instance.get_community(name=COMMUNITY_NAME)
    if response.status_code != 200:
        pytest.fail(f"{response.reason}")


def test_create_delete_post() -> None:

    instance = plemmy.LemmyHttp(INSTANCE_URL)
    instance.login(USERNAME, PASSWORD)
    response_create = instance.create_post(
        COMMUNITY_ID,
        f"Plemmy unit test {datetime.utcnow()}",
        "Unit test body text"
    )
    if response_create.status_code != 200:
        pytest.fail(f"{response_create.reason}")
    post_response = PostResponse(response_create)
    response_delete = instance.delete_post(
        True, post_response.post_view.post.id
    )
    if response_delete.status_code != 200:
        pytest.fail(f"{response_delete.reason}")


def test_create_delete_comment() -> None:

    instance = plemmy.LemmyHttp(INSTANCE_URL)
    instance.login(USERNAME, PASSWORD)
    response_post_create = instance.create_post(
        COMMUNITY_ID,
        f"Plemmy unit test {datetime.utcnow()}",
        "Unit test body text"
    )
    post_response = PostResponse(response_post_create)
    response_comment_create = instance.create_comment(
        f"Unit test comment {datetime.utcnow()}",
        post_response.post_view.post.id
    )
    if response_comment_create.status_code != 200:
        pytest.fail(f"{response_comment_create.reason}")
    instance.delete_post(
        True, post_response.post_view.post.id
    )
