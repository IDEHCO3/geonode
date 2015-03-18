from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('idehco3.layerEditor.views',
                       url(r'^$', TemplateView.as_view(template_name='layerEditor/index.html'), name='index'),
                       url(r'^new_layer$', 'new_layer', name='new_layer'),
                       url(r'^create_layer', 'create_layer', name='create_layer'))