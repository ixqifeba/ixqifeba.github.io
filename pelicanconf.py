#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ixqifeba'
SITENAME = 'wasurerareru'
SITEURL = '../'

PATH = 'content'
STATIC_PATHS = ['images']

# Int'l Settings
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = "themes/pure-single"
COVER_IMG_URL = '/images/eberhard-grossgasteiger-545770-unsplash.jpg'
TAGLINE = "documented moltings"
MENUITEMS = [
    ('About', './pages/about.html')
]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['./plugins'] #,  'themes/voce/plugins']
PLUGINS = []
