from django.conf.urls import patterns, url
from stocks import views

urlpatterns = patterns('',
                       url(r'^(?P<stock_ticker>[0-9]+)/$', views.detail, name='detail'),
#                       url(r'^(?P<stock_ticker>[0-9]+)/attachtag/$', views.attachtag, name='attachtag'),
                       url(r'^(?P<stock_ticker>[0-9]+)/daydata/$', views.dayData, name='dataData'),
#                       url(r'^tags/(?P<tag_id>[0-9]+)/$', views.tags, name='tags'),
                       url(r'^trades/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$', views.trades, name='trades'),
                       #Json calls
                       url(r'^(?P<stock_ticker>[0-9]+)/getdaydata/$', views.getDayData, name='getDayData'),
                       url(r'^webhook/$', views.webhook, name='webhook'),
                       url(r'^report/$', views.report, name='report'),
                       )