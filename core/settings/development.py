from core.settings.common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'TEST': {
            'ENGINE': 'django.db.backends.sqlite3',
        },
        'NAME': 'django_db',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': ''
    }
}

# psql -h localhost
# DROP DATABASE django_db; CREATE DATABASE django_db;
# \q

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'