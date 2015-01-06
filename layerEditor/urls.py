from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('layerEditor.views',
                       url(r'^$', TemplateView.as_view(template_name='layerEditor/index.html'), name='index'),
                       url(r'^new_layer$', 'new_layer', name='new_layer'))