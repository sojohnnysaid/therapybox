from core.settings.common import *
import django_heroku
import dj_database_url

DEBUG = os.getenv('DEBUG', False)

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Activate Django-Heroku.
django_heroku.settings(locals())