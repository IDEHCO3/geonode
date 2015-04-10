from django.conf.urls import patterns, url
from idehco3.community import views
from django.contrib.auth.decorators import login_required, permission_required
urlpatterns = patterns('idehco3.community',
    #urls para listar conhecimentos armazenados
    url(r'^$', views.CommunityList.as_view(), name='list'),
    url(r'^rest$', views.CommunityListRest.as_view(), name='list_rest'),
    url(r'detail/(?P<pk>\d+)/$', views.CommunityDetail.as_view(), name='detail'),
    url(r'create/$', login_required(views.CommunityCreate.as_view()), name='create'),
    url(r'update/(?P<pk>\d+)/$', views.CommunityUpdate.as_view(), name='update'),
    url(r'delete/(?P<pk>\d+)/$', views.CommunityDelete.as_view(), name='delete'),
    url(r'join_us/(?P<pk>\d+)/$', views.CommunityJoinUs.as_view(), name='join_us'),

)
