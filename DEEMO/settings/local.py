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

response = requests.get("https://mailtrap.io/api/v1/inboxes.json?api_token=" + "9b8bb8bfca740b8ff0b91cb642610cb0")
credentials = response.json()[0]
#DEFAULT_FROM_EMAIL = credentials['username']
#SERVER_EMAIL = credentials['username']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = credentials['domain']
EMAIL_HOST_USER = credentials['username']
EMAIL_HOST_PASSWORD = credentials['password']
EMAIL_PORT = credentials['smtp_ports'][0]
EMAIL_USE_TLS = True

INSTALLED_APPS += ['django.contrib.admin',]