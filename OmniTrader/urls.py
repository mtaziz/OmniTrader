from django.conf.urls import patterns, include, url
from django.contrib import admin
from stocks import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OmniTrader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stocks/', include('stocks.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)
