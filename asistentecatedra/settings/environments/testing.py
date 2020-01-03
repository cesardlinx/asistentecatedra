import os

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
DEBUG = True
ALLOWED_HOSTS = ['.localhost', '.asistentedecatedra.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": "db",
        "USER": "tester",
        "PASSWORD": "testing",
        "HOST": "localhost",
        "PORT": 5432
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
DOMAIN = 'localhost:8000'
MEDIA_ROOT = os.path.join(BASE_DIR, 'tests_media')

