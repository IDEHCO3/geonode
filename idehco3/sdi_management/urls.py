from django.conf.urls import patterns, url
from idehco3.sdi_management import views

urlpatterns = patterns('idehco3.sdi_management',
    #urls para listar conhecimentos armazenados
    url(r'^$', views.InstanceSDICoList.as_view(), name='list'),
    url(r'create/$', views.InstanceSDICoCreate.as_view(), name='create'),
    #url(r'update/(?P<pk>\d+)/$', views.CommunityUpdate.as_view(), name='update'),
    #url(r'delete/(?P<pk>\d+)/$', views.CommunityDelete.as_view(), name='delete'),

)
