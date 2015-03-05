try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

# place app url patterns here
urlpatterns = patterns('idehco3.tweeterStream.views',
                       url(r'^$', 'index', name='index'))