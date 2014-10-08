#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Salil Panikkaveettil'
SITENAME = u'AdMasterMind'
SITEURL = 'https://blog.admastermind.com'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('AdMasterMind', 'https://admastermind.com/'),)

# Social widget
SOCIAL = (
    ("LinkedIn", "http://in.linkedin.com/pub/salil-panikkaveettil/15/333/bba"),
    ("Facebook", "https://www.facebook.com/salilpa"),
    ("GitHub", "https://github.com/salilpa"),
    ("Google+", "https://plus.google.com/+SalilPanikkaveettil"),
    ("Twitter", "https://twitter.com/salilpa"),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
DISQUS_SITENAME = "admastermind"
GTM_ID = "GTM-WSW63N"
THEME = "themes/notmyidea"
