from .base import *

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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += ['django.contrib.admin',]