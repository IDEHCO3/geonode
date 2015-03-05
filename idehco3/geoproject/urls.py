from django.conf.urls import patterns, url
from idehco3.geoproject import views

urlpatterns = patterns('idehco3.geoproject',
    #urls para listar conhecimentos armazenados
    url(r'^$', views.GeoProjectList.as_view(), name='list'),
    #url(r'detail/(?P<pk>\d+)/$', views.CommunityDetail.as_view(), name='detail'),
    url(r'create/$', views.GeoProjectCreate.as_view(), name='create'),
    #url(r'update/(?P<pk>\d+)/$', views.CommunityUpdate.as_view(), name='update'),
    #url(r'delete/(?P<pk>\d+)/$', views.CommunityDelete.as_view(), name='delete'),

)
