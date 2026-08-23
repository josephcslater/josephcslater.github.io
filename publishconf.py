#!/usr/bin/env python
"""This file is only used if you use `make publish` or
explicitly specify it as your config file."""
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401,F403

SITEURL = 'http://josephcslater.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
