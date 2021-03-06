from .base import *  # noqa
from . import secrets


DEBUG = False
TEMPLATE_DEBUG = DEBUG
# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "seattle2015",
        "USER": "seattle2015",
        # ubuntu's default pg_hba.conf allows passwordless connections from localhost
        # when a user connects to a database with the same name as the user
    }
}

SITE_ID = 1

ALLOWED_HOSTS = ["confsite.pydata.org"]

SECRET_KEY = secrets.SECRET_KEY

EMAIL_BACKEND = secrets.EMAIL_BACKEND
EMAIL_USE_TLS = secrets.EMAIL_USE_TLS
EMAIL_HOST = secrets.EMAIL_HOST
EMAIL_HOST_USER = secrets.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = secrets.EMAIL_HOST_PASSWORD
EMAIL_PORT = secrets.EMAIL_PORT
