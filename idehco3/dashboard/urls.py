from django.conf.urls import patterns, url
from idehco3.dashboard import views

urlpatterns = patterns('idehco3.dashboard',
    #urls para listar conhecimentos armazenados
    url(r'^$', views.DashboardView.as_view(), name='dashboard_user'),
    #url(r'detail/(?P<pk>\d+)/$', views.CommunityDetail.as_view(), name='detail'),
    #url(r'update/(?P<pk>\d+)/$', views.CommunityUpdate.as_view(), name='update'),
    #url(r'delete/(?P<pk>\d+)/$', views.CommunityDelete.as_view(), name='delete'),

)

