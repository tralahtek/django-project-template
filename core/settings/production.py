from __future__ import absolute_import
import os
import django_heroku
import dj_database_url
from .common import *

DEBUG = False
DATABASES["default"] = dj_database_url.config(conn_max_age=900)
BROKER_URL = os.environ.get("REDIS_URL")

CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL"),
    }
}
django_heroku.settings(locals())
del DATABASES["default"]["OPTIONS"]["sslmode"]
