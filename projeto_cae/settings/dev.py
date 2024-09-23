from .base import *
import os

SECRET_KEY = 'django-insecure-6(7x$m_ik8qz5!xz6itr9ds&qvhrsnzrbkqiwwf$v!6eb-rb7h'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')