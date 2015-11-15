# Prod settings

from OmniTrader.settings import *
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = 'www.andrewmorro.com'


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
