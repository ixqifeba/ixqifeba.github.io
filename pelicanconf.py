#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ixqifeba'
SITENAME = 'wasurerareru'
SITEURL = 'http://localhost:8000/'

PATH = 'content'
PAGE_PATHS = ['pages']
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

# Look
THEME = "themes/pure-single"
#HIDE_CATEGORIES = True
COVER_IMG_URL = '/images/eberhard-grossgasteiger-545770-unsplash.jpg'
TAGLINE = "documented moltings"
POSTS_LIST = None  #options 'tags', 'categories', None
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('About', '/pages/about.html'),
    ('WIP', '/pages/drafts.html')
]

# What to render and how
ARTICLE_URL = 'done/{slug}/'
ARTICLE_SAVE_AS = 'done/{slug}/index.html'
DRAFT_URL = 'wip/{slug}.html'
DRAFT_SAVE_AS = 'wip/{slug}.html'
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
# render drafts listing
TEMPLATE_PAGES = {
    'drafts.html' : 'pages/drafts.html'
}

DISQUS_ON_PAGES = False
DEFAULT_PAGINATION = False
TYPOGRIFY = True
ARTICLE_ORDER_BY = 'reversed-date'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['./plugins'] #,  'themes/voce/plugins']
PLUGINS = []
