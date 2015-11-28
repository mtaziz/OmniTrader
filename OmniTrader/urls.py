from django.conf.urls import patterns, include, url
from django.contrib import admin
from stocks import views

import dropbox
import logging



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OmniTrader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stocks/', include('stocks.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)




logger = logging.getLogger('stocks.urls')

logger.info('Initiating OmniTrader')

logger.info("Linking to Dropbox account...")
dbx = dropbox.Dropbox('DO8936TNbkgAAAAAAAAAg4zB4LdJK2SBNBPdjaTWM5mpzjU8dFmp1MV5DNiEXDzk')