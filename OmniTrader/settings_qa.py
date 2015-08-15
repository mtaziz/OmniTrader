# QA settings

from OmniTrader.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'omnitrader-qa',
        'USER': 'omnitrader-qa',
        'PASSWORD': 'omnitraderq',
        'HOST': 'localhost',
        'PORT': '3306',
        'TEST_CHARSET': "utf8",
        'TEST_COLLATION': "utf8_general_ci",
        'CONN_MAX_AGE': None,
    }
}
