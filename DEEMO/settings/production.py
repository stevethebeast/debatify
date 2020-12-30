"""
Production Settings for Heroku
"""

import environ, requests

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

response = requests.get("https://mailtrap.io/api/v1/inboxes.json?api_token=" + env("MAILTRAP_API_TOKEN"))
credentials = response.json()[0]
DEFAULT_FROM_EMAIL = credentials['username']
SERVER_EMAIL = credentials['username']
EMAIL_HOST = credentials['domain']
EMAIL_HOST_USER = credentials['username']
EMAIL_HOST_PASSWORD = credentials['password']
EMAIL_PORT = credentials['smtp_ports'][0]
EMAIL_USE_TLS = env("EMAIL_USE_TLS")

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}