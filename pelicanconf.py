#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joseph C. Slater'
SITENAME = 'Inside the Ivory Tower'
SITEURL = 'http://josephcslater.github.io'
# josephcslater.github.io'

PATH = 'content'
BANNER = 'images/Alumni_Hall_1889_Sun.jpg'
BANNER_SUBTITLE = ''  # Inside the Ivory Tower
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_TAGS_ON_SIDEBAR = True
GITHUB_URL = 'http://github.com/josephcslater'
GITHUB_USER = 'josephcslater'
GITHUB_REPO_COUNT = 50
GITHUB_SHOW_USER_LINK = True
GITHUB_SKIP_FORK = True
TWITTER_USERNAME = '@JosephCSlater'
GOOGLE_ANALYTICS = 'UA-62100376-3'
DEFAULT_METADATA = {
    'status': 'draft',
}

# :Status: published

FIGURE_NUMBERS = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Website', 'https://josephcslater.github.io/josephcslater/'),
         ('Vibration Testing', 'https://github.com/Vibration-Testing'),
         ('Engineering Vibration Toolbox',
         'https://github.com/vibrationtoolbox'),)
#        ('Jinja2', 'http://jinja.pocoo.org/'),
#        ('You can modify those links in your config file', '#'),)


# Social widget
SOCIAL = (('LinkedIn', 'http://www.linkedin.com/in/JosephCSlater'),
          ('github', 'http://github.com/josephcslater'))

# Enables ipython notebook to work
# https://github.com/danielfrg/pelican-ipynb
MARKUP = ('md', 'ipynb')
# print(MARKUP)
PLUGIN_PATHS = './plugins'


# ----------------------
DEFAULT_PAGINATION = 10
TAG_CLOUD_MAX_ITEMS = 10
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
STATIC_PATHS = ['images', 'pdfs']
PAGE_PATHS = ['images', 'pdfs']
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False
FOUNDATION_ALTERNATE_FONTS = True
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = 'Powered by '
FOUNDATION_FOOTER_TEXT += '<a href="http://getpelican.com">Pelican</a> '
FOUNDATION_FOOTER_TEXT += 'and <a href="http://foundation.zurb.com/">Zurb '
FOUNDATION_FOOTER_TEXT += 'Foundation</a>.'
# Theme by <a href="http://hamaluik.com">Kenton Hamaluik</a>.'
FOUNDATION_PYGMENT_THEME = 'fruity'
PLUGIN_PATHS = ["/Users/jslater/websites/josephcslater/josephcslater.github.io/pelican/plugins",
"/Users/jslater/Documents/python-dev/plugins"]
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
PLUGINS = ['render_math', 'tag_cloud', 'ipynb.markup', 'i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
TAGS_URL = 'tags.html'
# PLUGINS = ["disqus_static"]
# PLUGINS = ['extract_toc','render_math','disqus_static',
#            'better_figures_and_images']


# PLUGINS = ['render_math', 'ipynb.liquid', 'tag_cloud']


DISQUS_SITENAME = "josephcslater"

DISQUS_SECRET_KEY = '0T8aMj8es19RuBKVVPVzzslKIdiCVWLPxZxOgexWCKfGTUMjQhaZYtd7yB6Rc2zn'
DISQUS_PUBLIC_KEY = 'y3C9OMSQLs5ovXENFwfUY3tLuI1GLBfmMteLjoeQpX9eICfXcoRyUJq8JZPjN336'

# DISQUS_SHORTNAME = 'josephcslater'
# MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
# THEME = "/Users/jslater/Documents/pelican-themes/foundation-default-colours"
# THEME = "/Users/jslater/Documents/pelican-themes/pure"
THEME = "/Users/jslater/Documents/python-dev/pelican-themes/pelican-bootstrap3"

# BOOTSTRAP_THEME =
# SITELOGO = 'images/JosephSlater8-11-cropped.jpg'
SITELOGO_SIZE = '60'
ABOUT_ME = 'Professor and Dean '
ABOUT_ME += 'at Tennessee Technological University. This blog contains '
ABOUT_ME += 'numerous, often unrelated, thoughts. I hope they may be of some '
ABOUT_ME += 'value to you.'
