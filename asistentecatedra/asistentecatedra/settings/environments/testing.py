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
