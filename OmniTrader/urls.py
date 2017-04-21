from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth.models import User
from stocks import views
from django.conf import settings
from rest_framework import routers, serializers, viewsets

import dropbox
import logging


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OmniTrader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stocks/', include('stocks.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    url(r'^autocomplete/', include('autocomplete_light.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns




logger = logging.getLogger('stocks.urls')

logger.info('Initiating OmniTrader')

#logger.info("Linking to Dropbox account...")
#dbx = dropbox.Dropbox('DO8936TNbkgAAAAAAAAAg4zB4LdJK2SBNBPdjaTWM5mpzjU8dFmp1MV5DNiEXDzk')
#dbx.users_get_current_account()