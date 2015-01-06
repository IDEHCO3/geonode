from django.conf.urls import patterns, url

urlpatterns = patterns('layerEditor.views',
                       url(r'^$', 'index', name='index'))