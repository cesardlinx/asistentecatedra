from split_settings.tools import optional, include
from decouple import config

ENV = config('DJANGO_ENV') or 'development'

base_settings = [
    "components/base.py",
    "components/ckeditor.py",
    "components/common.py",
    "components/database.py",
    "components/email.py",
    "components/security.py",

    'environments/{}.py'.format(ENV),
]

if ENV == 'development':
    base_settings.append(optional('environments/local.py'))

include(*base_settings)
