"""
Production Settings for Heroku
"""

import environ

# If using in your own project, update the project namespace below
from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    CORS_ALLOW_ALL_ORIGINS=(bool,False)
)

# False if not in os.environ
DEBUG = env('DEBUG')

ADMIN_ENABLED = env('ADMIN_ENABLED')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')

CORS_ALLOW_ALL_ORIGINS = env('CORS_ALLOW_ALL_ORIGINS')

DOMAIN = env('DOMAIN')

GOOGLE_RECAPTCHA_SECRET_KEY = env("GOOGLE_RECAPTCHA_SECRET_KEY")

MAILGUN_API_KEY = env("MAILGUN_API_KEY")
MAILGUN_DOMAIN = env("MAILGUN_DOMAIN")
MAILGUN_PUBLIC_KEY = env("MAILGUN_PUBLIC_KEY")
MAILGUN_SMTP_LOGIN = env("MAILGUN_SMTP_LOGIN")
MAILGUN_SMTP_PASSWORD = env("MAILGUN_SMTP_PASSWORD")
MAILGUN_SMTP_PORT = env("MAILGUN_SMTP_PORT")
MAILGUN_SMTP_SERVER = env("MAILGUN_SMTP_SERVER")
DEFAULT_FROM_EMAIL = env("MAILGUN_SMTP_LOGIN")
SERVER_EMAIL = env("MAILGUN_SMTP_LOGIN")
EMAIL_HOST = env("MAILGUN_DOMAIN")
#EMAIL_USE_TLS = True
#EMAIL_USE_SSL = False
EMAIL_PORT = env("MAILGUN_SMTP_PORT")
EMAIL_HOST_USER = env("MAILGUN_SMTP_LOGIN")
EMAIL_HOST_PASSWORD = env("MAILGUN_SMTP_PASSWORD")

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}