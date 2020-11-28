"""
Production Settings for Heroku
"""

import environ

# If using in your own project, update the project namespace below
from gettingstarted.settings.base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}

# import os
# from .base import *

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = get_secret_setting('SECRET_KEY')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

# ALLOWED_HOSTS = [
#     "damp-sea-29610.herokuapp.com",
#     "127.0.0.1",
#     "tlatter.gitlab.io",
# ]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': get_secret_setting('DATABASE_NAME'),
#         'USER': get_secret_setting('DATABASE_USER'),
#         'PASSWORD': get_secret_setting('DATABASE_PASSWORD'),
#         'HOST': get_secret_setting('DATABASE_HOST'),
#         'PORT': get_secret_setting('DATABASE_PORT'),
#     }
# }

# CORS_ALLOWED_ORIGINS = [
#     "https://tlatter.gitlab.io",
# ]

# # Heroku: Update database configuration from $DATABASE_URL.
# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)