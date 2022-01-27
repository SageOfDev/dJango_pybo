from .base import *

ALLOWED_HOSTS = ['3.35.145.231']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'qPKuKkq.a`&!]u!6bSZ+?FC54<J6gIU;',
        'HOST': 'ls-d432fd82043a84b76fd1d4c6820628e1d4067611.crnsvncee0lg.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}