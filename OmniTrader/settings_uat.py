# UAT settings

from OmniTrader.settings import *

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
    }
}
