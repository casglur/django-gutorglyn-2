import sys, os

import mimetypes

mimetypes.add_type("audio/ogg", ".ogg", True)

#print "__name__ =", __name__
#print "__file__ =", __file__
#print "os.getpid() =", os.getpid()
#print "os.getcwd() =", os.getcwd()
#print "os.curdir =", os.curdir
#print "sys.path =", repr(sys.path)
#print "sys.modules.keys() =", repr(sys.modules.keys())
#print "sys.modules.has_key('mysite') =", sys.modules.has_key('mysite')
#if sys.modules.has_key('mysite'):
#    print "sys.modules['mysite'].__name__ =", sys.modules['mysite'].__name__
#    print "sys.modules['mysite'].__file__ =", sys.modules['mysite'].__file__
#    print "os.environ['DJANGO_SETTINGS_MODULE'] =", os.environ.get('DJANGO_SETTINGS_MODULE', None)
  
# Django settings for sdpublisher project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	(('Alexander', 'a.l.roberts@swansea.ac.uk'), ('Alexander','damokleaze@hotmail.com'))
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'django.db.backends.mysql'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'gutorglyn'             # Or path to database file if using sqlite3.
DATABASE_USER = 'gutorglyn'             # Not used with sqlite3.
DATABASE_PASSWORD = '3riublev'         # Not used with sqlite3.
DATABASE_HOST = '127.0.0.1'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '3306'             # Set to empty string for default. Not used with sqlite3.



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'cy-GB'

#ugettext = lambda s: s

LANGUAGES = (
    ('cy-GB', 'Welsh'),             
    ('en-GB', 'English'),
)

LANGUAGE_COOKIE_NAME = 'gutorglynlang'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n8_1&im$-h8l&^=921q*re3)@z9^zd)n50fa0%0gsy)bnv*(2='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

STATIC_ROOT = '/SDPublisher/SDPublisher/static'

STATIC_URL = "/static/"

STATICFILES_DIRS = (
	'/SDPublisher/SDPublisher/gutorglyn/static',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/static/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

FORCE_SCRIPT_NAME = ""

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',    
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'SDPublisher.pixelise',
    'SDPublisher.SDPintro',
    'SDPublisher.origin',
    'SDPublisher.gutorglyn',
    'SDPublisher.white',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },         
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
             # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },   
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/django/gutorglyn.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            'formatter': 'verbose'
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
            'formatter': 'verbose'            
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'SDPublisher': {
            'handlers': ['logfile'],
            'level': 'WARNING', # Or maybe INFO or DEBUG
            'propagate': False,
            'formatter': 'verbose'            
        },
    },
}

