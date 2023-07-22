# Plemmy: a Python package for accessing the Lemmy API

<img src="https://github.com/tjkessler/plemmy/blob/main/img/plemmy.png" alt="drawing" width="325"/>

[![GitHub version](https://badge.fury.io/gh/tjkessler%2Fplemmy.svg)](https://badge.fury.io/gh/tjkessler%2Fplemmy)
[![PyPI version](https://badge.fury.io/py/plemmy.svg)](https://badge.fury.io/py/plemmy)
[![GitHub license](https://img.shields.io/badge/license-Apache-blue.svg)](https://raw.githubusercontent.com/tjkessler/plemmy/master/LICENSE.txt)

Plemmy allows you to interact with any Lemmy instance using Python and the [LemmyHttp API](https://join-lemmy.org/api/classes/LemmyHttp.html).

**WARNING:** Plemmy is still in development and needs testing!

## Installation ##

For the most up-to-date version of Plemmy, clone and install from the repository:

```
git clone https://github.com/tjkessler/plemmy
cd plemmy
python setup.py install
```

A PyPI repository is periodically updated:

```
pip install plemmy
```

## Basic usage ##

Interact with a Lemmy instance using the _LemmyHttp_ object:

```python
from plemmy import LemmyHttp

# create object for Lemmy.ml, log in
srv = LemmyHttp("https://lemmy.ml")
srv.login("<username_or_email>", "<password>")
```

Access specific communities:

```python
from plemmy.responses import GetComunityResponse

# obtain community, parse JSON
api_response = srv.get_community(name="Lemmy")
response = GetCommunityResponse(api_response)

# community info
community = response.community_view.community
print(community.name)
print(community.actor_id)
print(community.id)

# list community moderators
for person in response.moderators:
    print(person.moderator.name, person.community.name)
```

Create a post:
```python
from plemmy.responses import PostResponse

# create post, parse JSON
api_response = srv.create_post(community.id, "Test post please ignore", "Body text")
response = PostResponse(api_response)

# post info
post = response.post_view.post
print(post.creator_id)
print(post.community_id)
print(post.name)
print(post.body)
```

Full documentation is on its way, but in the meantime check out our source code and some [examples](https://github.com/tjkessler/plemmy/tree/main/examples).

## Reporting issues, making contributions, etc. ##

Don't hesitate to report a bug or unexpected results! Want to contribute? Make a pull request. Contact [@tjkessler](https://github.com/tjkessler) with any questions.
