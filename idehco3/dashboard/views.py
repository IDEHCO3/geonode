from django.views.generic import TemplateView
from idehco3.community.models import Community, MembershipCommunity
from idehco3.dashboard import models
from django.views import generic
from idehco3.dashboard.models import Dashboard


class DashboardView(TemplateView):

    template_name = "dashboard/dashboard_list.html"

    model = Dashboard

    authenticated_user = None

    def get(self, request, *args, **kwargs):

       self.authenticated_user = request.user

       return super(DashboardView, self).get(self, request, *args, **kwargs)

    def communities(self):

        msc_list = MembershipCommunity.objects.filter(member=self.authenticated_user)

        communities = (msc.community for msc in msc_list)

        return communities






