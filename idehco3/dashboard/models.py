from django.db import models
import geonode
from idehco3.base.models import Invitation, Action, Membership
from idehco3.community.models import Community, MembershipCommunity


class Dashboard(models.Model):

    information = models.CharField(null=True, max_length=100)

    user = models.ForeignKey(geonode.settings.AUTH_USER_MODEL)

    def communities(self):

        #memberships = MembershipCommunity.objects.filter(user__id = self.user_id)

        memberships =  MembershipCommunity.objects.all()

        list = []

        for ms in memberships:
            list.append(ms.community)


        return list



