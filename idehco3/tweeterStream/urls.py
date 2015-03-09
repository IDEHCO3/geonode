try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from idehco3.tweeterStream.views import *

# place app url patterns here
urlpatterns = patterns('idehco3.tweeterStream.views',
                       url(r'^$', TweeterStreamList.as_view(), name='list'),
                       url(r'^detail/(?P<pk>\d+)/', TweeterStreamDetail.as_view(), name='detail'),
                       url(r'^create', TweeterStreamCreate.as_view(), name='create'),
                       url(r'^update/(?P<pk>\d+)/', TweeterStreamUpdate.as_view(), name='update'),
                       url(r'^delete/(?P<pk>\d+)/', TweeterStreamDelete.as_view(), name='delete'))