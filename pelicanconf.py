#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ResilientTx'
SITENAME = u'Proof of Audit'
SITEURL = ''
ABOUTPAGE = '/pages/about-us.html#home'
MENUITEMS =[]
PATH = 'content'

TIMEZONE = 'America/Dawson'

THEME = "themes/simple"


DEFAULT_LANG = u'en'

STATIC_PATHS = [
    'static',
]

ARTICLE_EXCLUDES = [
    'static'
]

DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = None

DISPLAY_PAGES_ON_MENU = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
