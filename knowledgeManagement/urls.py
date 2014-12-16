from django.conf.urls import patterns, url

urlpatterns = patterns('',
    #KM
    #urls para listar conhecimentos armazenados
    url(r'^$', 'knowledgeManagement.views.index', name='index'),
    url(r'^(?P<knowledge_id>\d+)/$', 'knowledgeManagement.views.detail', name='detail'),
    url(r'^(?P<map_id>\d+)/get_map_knowledge/$', 'knowledgeManagement.views.getMapKnowledge'),
    url(r'^(?P<layer_id>\d+)/get_layer_knowledge/$', 'knowledgeManagement.views.getLayerKnowledge'),
    #urls para armazenar novos conhecimentos    
    url(r'^put_knowledge/$', 'knowledgeManagement.views.putKnowledge', name='inputKnowledge'),
    #url(r'^knowledgeManagement/(?P<layer_id>\d+)/put_layer_knowledge/$', 'knowledgeManagement.views.putLayerKnowledge'),
)