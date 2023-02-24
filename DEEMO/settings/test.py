from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMIN_ENABLED = False

ALLOWED_HOSTS = []

DATABASES = {
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'postgres',
        'PORT': '',
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'USER': 'djangodb',
        'PASSWORD': 'horsehorsehorse',
        'HOST': 'localhost',
        'PORT': '',
    }
}

CORS_ALLOWED_ORIGINS = []

DOMAIN = "http://127.0.0.1:8000"

REST_SAFE_LIST_IPS = ['ALLOW_ALL']

LOGIN_PROVIDED = True

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
