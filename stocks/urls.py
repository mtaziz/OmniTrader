from django.conf.urls import patterns, include, url
from stocks import views
from stocks.views.StockViews import StockByTicker,StockByTags



urlpatterns = patterns('',
                       url('^(?P<ticker>[0-9]+)/$', StockByTicker.as_view()),
                       url('^tags/(?P<tags>.+)/$', StockByTags.as_view()),
                       url(r'^(?P<stock_ticker>[0-9]+)/daydata/$', views.dayData, name='dataData'),
#                       url(r'^tags/(?P<tag_id>[0-9]+)/$', views.tags, name='tags'),
                       url(r'^trades/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$', views.trades, name='trades'),
                       #Json calls
                       url(r'^webhook/$', views.webhook, name='webhook'),
                       url(r'^report/$', views.report, name='report'),
                       )