from decouple import config
import os
from os.path import join  # noqa F401

DJANGO_ENV = config('DJANGO_ENV')
PROTOCOL = config('PROTOCOL')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'accounts',
    'planificaciones',
    'asistente',
    'ckeditor',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

SITE_ID = 1

ROOT_URLCONF = 'asistentecatedra.urls'

WSGI_APPLICATION = 'asistentecatedra.wsgi.application'

MEDIA_URL = '/assets/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ALLOWED_UPLOAD_IMAGES = ('gif', 'bmp', 'jpeg', 'jpg', 'png')

MIGRATION_MODULES = {
    'sites': 'asistentecatedra.fixtures.sites_migrations',
}

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/planificaciones/'
