from .base import *
import os, requests

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8p=sgre$q3%9fc7dw#e2k0$xtrfyx=@4a(1yhd!rbdkun91nq^'

GOOGLE_RECAPTCHA_SECRET_KEY = "6LfGCBcaAAAAAGZV486tW3qq4tGNehToaRC6WogO"

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

DEFAULT_FROM_EMAIL = "account.confimation@debatify.co"
SERVER_EMAIL = "account.confimation@debatify.co"
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "mail.debatify.co"
EMAIL_HOST_USER = "account.confimation@debatify.co"
EMAIL_HOST_PASSWORD = "k-BebiFunX3g"
EMAIL_PORT = 587
EMAIL_USE_TLS = False

REST_SAFE_LIST_IPS = ['ALLOW_ALL']

LOGIN_PROVIDED = True

INSTALLED_APPS += ['django.contrib.admin',]