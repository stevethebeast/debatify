from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret_setting('DATABASE_TEST_NAME'),
        'USER': get_secret_setting('DATABASE_TEST_USER'),
        'PASSWORD': get_secret_setting('DATABASE_TEST_PASSWORD'),
        'HOST': get_secret_setting('DATABASE_TEST_HOST'),
        'PORT': get_secret_setting('DATABASE_TEST_PORT'),
    }
}

CORS_ALLOWED_ORIGINS = []