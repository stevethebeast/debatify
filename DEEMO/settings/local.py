from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8p=sgre$q3%9fc7dw#e2k0$xtrfyx=@4a(1yhd!rbdkun91nq^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMIN_ENABLED = True

ALLOWED_HOSTS = []

DATABASES = {
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

DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")
SERVER_EMAIL = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

INSTALLED_APPS += ['django.contrib.admin',]