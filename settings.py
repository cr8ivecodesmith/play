from __future__ import unicode_literals

AUTHOR = 'matt lebrun'
SITENAME = 'the playground'
TAGLINE = 'An exercise for the creative and imaginative mind.'
USER_LOGO_URL = 'http://www.gravatar.com/avatar/0f0e8de906724bbb54093f1852e7522e.png?size=140x140'
SITEURL = 'http://play.mattlebrun.com'
DEFAULT_DATE_FORMAT = '%A, %B %d, %Y'
SUMMARY_MAX_LENGTH = (50)

GITHUB_URL = 'https://github.com/cr8ivecodesmith/play'
DISQUS_SITENAME = 'cr8ivecodesmith'

# TODO: Create a new GA ID for this site.
# GOOGLE_ANALYTICS = 'UA-9679489-4'

FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

SOCIAL = (('@cr8ivecodesmith', 'https://twitter.com/cr8ivecodesmith'),
          ('blog', 'http://mattlebrun.com'),
          ('email', 'mailto:lebrun.matt@gmail.com'),)
TWITTER_USERNAME = 'cr8ivecodesmith'

THEME = '.pelican_themes/pelican-svbhack'
TIMEZONE = 'Asia/Manila'
DEFAULT_PAGINATION = 3

MARKUP = (('md', 'rst'))
MD_EXTENSIONS = (['codehilite', 'extra'])
