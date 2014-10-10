#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'vinaykola'
SITENAME = u'infiniteimprobability'
SITEURL = 'http://vinaykola.com'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/vinaykola'),
          ('github', 'http://github.com/vinaykola'),
          ('linkedin', 'http://linkedin.com/in/vinaykola'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extras/vinaykola_resume.pdf']

EXTRA_PATH_METADATA = {
    'extras/vinaykola_resume.pdf': {'path': 'vinaykola_resume.pdf'}
}
