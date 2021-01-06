from core.settings.common import *
import django_heroku
import dj_database_url

DEBUG = os.getenv('DEBUG', False)

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}


AWS_ACCESS_KEY_ID = os.getenv('BUCKETEER_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('BUCKETEER_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('BUCKETEER_BUCKET_NAME')
AWS_REGION = os.getenv('BUCKETEER_AWS_REGION')

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
# Activate Django-Heroku.
django_heroku.settings(locals())