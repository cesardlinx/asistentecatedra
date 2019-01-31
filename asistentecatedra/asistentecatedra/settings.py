import os
from os.path import join  # noqa F401

from decouple import Csv, config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROTOCOL = config('PROTOCOL')
DOMAIN = config('DOMAIN')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# CKEditor configuration
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_CustomToolbarConfig': [

            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                       'Superscript', '-', 'RemoveFormat']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar',
                       'PageBreak']},
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent',
                       'Indent', '-', 'Blockquote', '-', 'JustifyLeft',
                       'JustifyCenter', 'JustifyRight', 'JustifyBlock',
                       '-', 'BidiLtr', 'BidiRtl']},
        ],
        'toolbar': 'CustomToolbarConfig',  # put selected toolbar config here
        'width': '99%',
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'autogrow',
        ]),
    },
    'basic': {
        'skin': 'moono',
        'toolbar_CustomToolbarConfig': [

            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                       'Superscript', '-', 'RemoveFormat']},
            {'name': 'insert',
             'items': ['SpecialChar']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
            ]},
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent',
                       'Indent', '-', 'JustifyLeft',
                       'JustifyCenter', 'JustifyRight', 'JustifyBlock',
                       '-', 'BidiLtr', 'BidiRtl']},
        ],
        'toolbar': 'CustomToolbarConfig',  # put selected toolbar config here
        'width': '99%',
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'autogrow',
        ]),
    }
}

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
    'ckeditor_uploader',
    'widget_tweaks'
]

SITE_ID = config('SITE_ID', cast=int)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'asistentecatedra.urls'

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

WSGI_APPLICATION = 'asistentecatedra.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int)
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa E501
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es-ec'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [  # noqa F811
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# User model
AUTH_USER_MODEL = 'accounts.User'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = True

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa E501
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa E501
    },
    {'NAME': 'accounts.validators.NumberValidator', },
    {'NAME': 'accounts.validators.UppercaseValidator', },
    {'NAME': 'accounts.validators.LowercaseValidator', },
]

# Recaptcha
GOOGLE_RECAPTCHA_SECRET_KEY = config('GOOGLE_RECAPTCHA_SECRET_KEY')
