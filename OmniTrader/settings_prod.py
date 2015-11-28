# Prod settings

from OmniTrader.settings import *
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = 'trade.andrewmorro.com'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'omnitrader',
        'USER': 'omnitrader',
        'PASSWORD': 'omnitraderp',
        'HOST': 'cragguidebook.mysql.rds.aliyuncs.com',
        'PORT': '3306'
    }
}

STATIC_ROOT = '/opt/static'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/OmniTrader/prod.log',
        },
    },
    'root': {
        'handlers': ['file','console'],
        'level': 'INFO',
    },
}
