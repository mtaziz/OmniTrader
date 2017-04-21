# UAT settings

from OmniTrader.settings import *

#DEBUG = False
#ALLOWED_HOSTS = ['127.0.0.1','localhost']

LOG_LEVEL = 'INFO'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'omnitrader-qa',
        'USER': 'omnitraderq',
        'PASSWORD': 'omnitraderq',
        'HOST': 'cragguidebook.mysql.rds.aliyuncs.com',
        'PORT': '3306',
        'TEST_CHARSET': "utf8",
        'TEST_COLLATION': "utf8_general_ci",
        'CONN_MAX_AGE': 36000,
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    }
}