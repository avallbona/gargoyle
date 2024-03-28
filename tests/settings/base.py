import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'NOTASECRET'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev-database.sqlite3',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'testapp',
    'gargoyle',
    'nexus',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
)

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'

GARGOYLE_SWITCH_DEFAULTS = {
    'active_by_default': {
        'is_active': True,
        'label': 'Default Active',
        'description': 'When you want the newness',
    },
    'inactive_by_default': {
        'is_active': False,
        'label': 'Default Inactive',
        'description': 'Controls the funkiness.',
    },
    'selective_by_default': {
        'initial_status': 2,  # SELECTIVE - import error on Django 1.8 prevents us importing from gargoyle.constants
        'label': 'Default Inactive',
        'description': 'Controls more funkiness.',
    },
}
