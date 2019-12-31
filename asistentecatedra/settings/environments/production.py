from decouple import config

DEBUG = False
ALLOWED_HOSTS = ['.asistentedecatedra.com']
ADMINS = (('Administrator', 'admin@asistentedecatedra.com'),)
MANAGERS = ADMINS
PROTOCOL = 'https'
DOMAIN = 'asistentedecatedra.com'

SUPERUSER_EMAIL = config('SUPERUSER_EMAIL')
SUPERUSER_PASSWORD = config('SUPERUSER_PASSWORD')
SUPERUSER_FIRSTNAME = config('SUPERUSER_FIRSTNAME')
SUPERUSER_LASTNAME = config('SUPERUSER_LASTNAME')
