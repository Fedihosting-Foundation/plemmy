# Plemmy: a Python package for accessing the Lemmy API

<img src="img/plemmy.png" alt="drawing" width="325"/>

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

# create object for Lemmy.ml
srv = LemmyHttp("https://lemmy.ml")

# log in to Lemmy.ml
srv.login("<username_or_email>", "<password>")

# make a comment
srv.create_comment("Hello from plemmy!", post_id)

# create a post
srv.create_post(community_id, "New post's title", body="Body text", url="https://a.link.to.share")
```

Full documentation is on its way, but in the meantime check out our source code.

## Reporting issues, making contributions, etc. ##

Don't hesitate to report a bug or unexpected results! Want to contribute? Make a pull request. Contact [@tjkessler](https://github.com/tjkessler) with any questions.
