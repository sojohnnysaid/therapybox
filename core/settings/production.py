from core.settings.common import *
import django_heroku
import dj_database_url

DEBUG = os.getenv('DEBUG', False)

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}


AWS_ACCESS_KEY_ID = os.getenv('BUCKETEER_AWS_ACCESS_KEY_ID')
AWS_REGION = os.getenv('BUCKETEER_AWS_REGION')
AWS_SECRET_ACCESS_KEY = os.getenv('BUCKETEER_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('BUCKETEER_BUCKET_NAME')

STATIC_URL = 'https://bucketeer-fa1dfd61-3784-458d-9907-4183fff80084.s3.amazonaws.com/public/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# Activate Django-Heroku.
django_heroku.settings(locals())