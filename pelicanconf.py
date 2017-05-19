#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'International Union for Conservation of Nature and UN Environment World Conservation Monitoring Centre'
SITENAME = u'World Heritage Datasheet'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# additional ========
ARTICLE_URL = 'site/{slug}'
ARTICLE_SAVE_AS = 'site/{slug}/index.html'

HIDE_SIDEBAR = True
DISPLAY_CATEGORIES_ON_MENU = False

# A list of tuples (Title, URL) for additional menu items to appear at the beginning of the main menu.
COLLAPSE_NAVBAR = True
MENUITEMS = [('Country', SITEURL + '/tags')]

JINJA_EXTENSIONS = ['jinja2.ext.i18n']

THEME = r"pelican-bootstrap3"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search', 'pelican-toc']

TOC = {
    'TOC_HEADERS' : '^h[2-6]',  # What headers should be included in the generated toc
                                # Expected format is a regular expression

    'TOC_RUN'     : 'true'      # Default value for toc generation, if it does not evaluate
                                # to 'true' no toc will be generated
}

# search enabled
DIRECT_TEMPLATES = ('index', 'tags', 'search')

LOAD_CONTENT_CACHE = False

TYPOGRIFY = True

GOOGLE_ANALYTICS = 'UA-61833965-5'
