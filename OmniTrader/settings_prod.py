# Prod settings

from OmniTrader.settings import *
#INTERNAL_IPS = '101.87.65.96,116.251.217.104'
DEBUG = False
TEMPLATE_DEBUG = False
#allow amazonaws for dropbox push
ALLOWED_HOSTS = ['.andrewmorro.com','localhost','.dropbox.com']
#ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'omnitrader',
        'USER': 'omnitrader',
        'PASSWORD': 'omnitraderp',
        'HOST': 'cragguidebook.mysql.rds.aliyuncs.com',
        'PORT': '3306',
        'TEST_CHARSET': "utf8",
        'TEST_COLLATION': "utf8_general_ci",
        'CONN_MAX_AGE': 36000,
    }
}

STATIC_ROOT = '/opt/static'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters' : {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s: %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '[%(levelname)-7s] %(asctime)s - %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*5,  # 10 MB
            'backupCount': 20,
            'formatter': 'simple',
            'filename': '/var/log/OmniTrader/prod.log',
            'encoding': 'utf8',
        },
    },
    'root': {
        'handlers': ['file','console'],
        'level': 'INFO',
    },
}
