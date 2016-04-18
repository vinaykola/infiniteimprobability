#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vinay Kola'
SITENAME = u'Infinite Improbability'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/vinaykola'),
          ('github', 'http://github.com/vinaykola'),
          ('linkedin', 'http://linkedin.com/in/vinaykola'))

DEFAULT_PAGINATION = 10

THEME = 'themes/pelican-svbhack'

TAGLINE = 'Infinite Improbability • Musings about life and programming • Work @ Snapchat'

USER_LOGO_URL = SITEURL + '/images/vinaykola.png'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
