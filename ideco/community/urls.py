from django.conf.urls import patterns, url
from ideco.community import views

urlpatterns = patterns('ideco.community',
    #urls para listar conhecimentos armazenados
    url(r'^$', views.CommunityList.as_view(), name='list'),
    url(r'detail/(?P<pk>\d+)/$', views.CommunityDetail.as_view(), name='detail'),
    url(r'create/$', views.CommunityCreate.as_view(), name='create'),
    url(r'update/(?P<pk>\d+)/$', views.CommunityUpdate.as_view(), name='update'),
    url(r'delete/(?P<pk>\d+)/$', views.CommunityDelete.as_view(), name='delete'),

)
