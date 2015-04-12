from django.conf.urls import patterns, url
from stocks import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<stock_id>[0-9]+)/$', views.detail, name='detail'),
                       url(r'^tags/(?P<tag_id>[0-9]+)/$', views.tags, name='tags'),
                       )