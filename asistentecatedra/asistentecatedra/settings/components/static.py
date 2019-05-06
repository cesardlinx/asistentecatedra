import os
from os.path import join  # noqa F401

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [  # noqa F811
    os.path.join(BASE_DIR, 'static')
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'npm.finders.NpmFinder',
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
