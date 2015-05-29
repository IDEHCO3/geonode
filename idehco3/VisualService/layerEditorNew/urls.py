try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.views.generic import TemplateView


# place app url patterns here
urlpatterns = patterns('idehco3.VisualService.layerEditorNew.views',
                       url(r'^$', 'testEditorLayerNew', name='index'))