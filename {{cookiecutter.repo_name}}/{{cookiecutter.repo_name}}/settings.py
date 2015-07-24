"""
Django settings for {{ cookiecutter.project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/
"""


import os
from os.path import join, abspath, dirname
gettext = lambda s: s
import dj_database_url



here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here('..',)
root = lambda *x: join(abspath(PROJECT_ROOT), *x)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# People who get code error notifications.
# In the format (('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com'))
ADMINS = ()

# Tuple of IP addresses, as strings, that:
# * See debug comments, when DEBUG is true
# * Receive x-headers
INTERNAL_IPS = ('127.0.0.1', '::1', '0.0.0.0')

# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SITE_ID = 1

CMS_PERMISSION = True

# Local time zone for this installation. All choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name (although not all
# systems may support all possibilities). When USE_TZ is True, this is
# interpreted as the default user time zone.
TIME_ZONE = 'Europe/Madrid'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

# The django CMS allows you to edit all languages for which Django has
# built in translations. Since these are numerous, we’ll limit it to English for now:
LANGUAGES = (
    ('en', gettext('english')),
    ('es', gettext('spanish')),
    ('gl', gettext('galician')),
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('English'),
        },

        {
            'code': 'es',
            'name': gettext('Spanish'),
        },

        {
            'code': 'gl',
            'name': gettext('Galician'),

        },
    ],
    'default': {
        'fallbacks': ['en', 'es', 'gl'],
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
}

PARLER_LANGUAGES = {
    1: (
        {'code': 'en',},
        {'code': 'es',},
        {'code': 'gl',},
    ),
    'default': {
        'fallback': 'en',             # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
    }
}

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to True, Django will format dates, numbers and calendars
# according to user current locale.
USE_L10N = True

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Application definition
INSTALLED_APPS = (
    'djangocms_admin_style', # Before 'django.contrib.admin' entry
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'djangocms_text_ckeditor', # Before 'cms' entry
    'cms',
    'menus',
    'sekizai',
    'filer',
    'mptt',
    'treebeard',
    'parler',

    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    'storages',
    'djangocms_link',
    'easy_thumbnails',
    'reversion',
    'django_extensions',
    'braces',
    'taggit',
    # 'debug_toolbar',
)

# List of locations of the template source files, in search order.
TEMPLATE_DIRS = (
    root('templates'),
)

# Add at least one template to CMS_TEMPLATES
CMS_TEMPLATES = (
    ('main.html', 'Main template'),
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

# List of middleware classes to use. Order is important; in the request phase,
# this middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{ cookiecutter.repo_name }}.wsgi.application'

MEDIA_ROOT = root('media')


###############
# STATICFILES #
###############

# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = root('staticfiles')

# A list of locations of additional static files
STATICFILES_DIRS = (
    root('static'),
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if DEBUG == False:
    STATIC_ROOT = "/static/"
    MEDIA_ROOT = "/media/"

    # DEFAULT_FILE_STORAGE = 'myapp.s3utils.S3MediaStorage'
    # STATICFILES_STORAGE = 'myapp.s3utils.S3StaticStorage'

    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
    AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')


    STATIC_URL = 'http://{}.s3.amazonaws.com/static/'.format(AWS_BUCKET_NAME)
    MEDIA_URL = 'http://{}.s3.amazonaws.com/media/'.format(AWS_BUCKET_NAME)


    AWS_REDUCED_REDUNDANCY = False # We enable this server-wide on our staging server's S3 buckets
    AWS_PRELOAD_METADATA = True # You want this to be on!
    AWS_S3_SECURE_URLS = False
    AWS_HEADERS = { 'Cache-Control': 'max-age=2592000' }
    AWS_QUERYSTRING_AUTH = False



########################
# DJANGO DEBUG TOOLBAR #
########################

# Tell the toolbar not to adjust your settings automatically
# DEBUG_TOOLBAR_PATCH_SETTINGS = False


################
# django-filer #
################

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

MIGRATION_MODULES = {
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}
