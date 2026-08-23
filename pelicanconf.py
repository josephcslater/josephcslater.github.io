#!/usr/bin/env python
"""Pelican configuration for 'Inside the Ivory Tower'."""
import os

from pelican import signals


def _restore_short_plugin_names(pelican_object):
    """Compatibility shim for themes (e.g. pelican-bootstrap3) that check
    for legacy short plugin names such as 'tag_cloud' in PLUGINS. Modern
    namespace-package plugins are recorded under their full dotted path
    (e.g. 'pelican.plugins.tag_cloud'), so add the short aliases back.
    """
    plugin_names = pelican_object.settings.get('PLUGINS', [])
    short_names = [name.rsplit('.', 1)[-1] for name in plugin_names if '.' in name]
    pelican_object.settings['PLUGINS'] = plugin_names + [
        name for name in short_names if name not in plugin_names
    ]


class PluginNameCompat:
    """A minimal in-line plugin; see _restore_short_plugin_names above."""

    @staticmethod
    def register():
        signals.initialized.connect(_restore_short_plugin_names)


AUTHOR = 'Joseph C. Slater'
SITENAME = 'Inside the Ivory Tower'
SITEURL = 'https://josephcslater.github.io'

PATH = 'content'
BANNER = 'images/Alumni_Hall_1889_Sun.jpg'
BANNER_SUBTITLE = ''
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_TAGS_ON_SIDEBAR = True
GITHUB_URL = 'https://github.com/josephcslater'
GITHUB_USER = 'josephcslater'
GITHUB_REPO_COUNT = 50
GITHUB_SHOW_USER_LINK = True
GITHUB_SKIP_FORK = True
TWITTER_USERNAME = '@JosephCSlater'
GOOGLE_ANALYTICS = 'UA-62100376-3'
DEFAULT_METADATA = {
    'status': 'draft',
}

FIGURE_NUMBERS = True

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Website', 'https://josephcslater.github.io/josephcslater/'),
    ('Vibration Testing', 'https://github.com/Vibration-Testing'),
    ('Engineering Vibration Toolbox', 'https://github.com/vibrationtoolbox'),
)

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/JosephCSlater'),
    ('github', 'https://github.com/josephcslater'),
)

DEFAULT_PAGINATION = 10
TAG_CLOUD_MAX_ITEMS = 10
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
STATIC_PATHS = ['images', 'pdfs']
PAGE_PATHS = ['images', 'pdfs']

ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
TAGS_URL = 'tags.html'

# 'render_math', 'tag_cloud' and 'i18n_subsites' are installed from PyPI
# (pelican-render-math, pelican-tag-cloud, pelican-i18n-subsites) and are
# auto-discovered via the pelican.plugins namespace, so no PLUGIN_PATHS
# is required.
PLUGINS = ['render_math', 'tag_cloud', 'i18n_subsites', PluginNameCompat]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

DISQUS_SITENAME = 'josephcslater'
# Never hard-code secrets in tracked source. Set these in your shell/CI
# environment instead, e.g.:
#   export PELICAN_DISQUS_SECRET_KEY=...
#   export PELICAN_DISQUS_PUBLIC_KEY=...
DISQUS_SECRET_KEY = os.environ.get('PELICAN_DISQUS_SECRET_KEY', '')
DISQUS_PUBLIC_KEY = os.environ.get('PELICAN_DISQUS_PUBLIC_KEY', '')

# Theme lives in a separate checkout of the pelican-themes collection.
# Override with the PELICAN_THEME_DIR environment variable if your
# checkout lives elsewhere.
THEME = os.environ.get(
    'PELICAN_THEME_DIR',
    os.path.expanduser('~/Documents/python-dev/pelican-themes/pelican-bootstrap3'),
)

SITELOGO_SIZE = '60'
ABOUT_ME = (
    'Professor and Dean at Tennessee Technological University. This blog '
    'contains numerous, often unrelated, thoughts. I hope they may be of '
    'some value to you.'
)
