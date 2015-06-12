from django.db import models
import datetime
# Create your models here.
#from geonode.people.models import Profile
import geonode
from geonode.people.models import Profile
import idehco3
from idehco3.base.models import Invitation, Action, Membership
from geonode.layers.models import Layer
from idehco3.utils.utils import getGeoJsonURLFromLayer
from django.contrib.gis.db import models as modelsGis
from django_pgjson.fields import JsonBField


class Community(models.Model):

    name = models.CharField(max_length = 150)

    description = models.TextField(null=True, blank=True)

    need_invitation = models.BooleanField(default=False)

    date_creation = models.DateTimeField(default=datetime.datetime.now(), null=True)

    #members = models.ManyToManyField(geonode.settings.AUTH_USER_MODEL, through='MembershipCommunity', related_name='communities')

    owner = models.ForeignKey(geonode.settings.AUTH_USER_MODEL,related_name='owner_of_community', db_column='id_manager')

    def not_need_invitation(self):

        return not self.need_invitation

    def can_join(self):

        self

    def members(self):

        return (ms.member for ms in self.membership_list)

    def users(self):
        return self.members()

    def __unicode__(self):
        return self.name

    def invite_someone_to_community(self):
        pass

    def invite_user_to_community(self, inviter_user, invited_user):

        invitation = Invitation()

        invitation.inviter = inviter_user

        act = Action()

        act.receiver_message_parameter(self, 'join_us', invited_user )

        act.save()

        invitation.action = act

        invitation.save()


    def manager_community(self):
        pass

    def remove_user(self, a_member):

        self.members.remove(a_member)

    def join_us(self, interested_user, an_invite_reason='Join us'):

        membership = MembershipCommunity()

        if membership.is_not_included(interested_user, self):

            membership.join_us(interested_user, self, an_invite_reason)

            membership.save()

            return membership

        return None

    def get_main_layer(self):
        composer = self.composer_community.all()
        if composer:
            return composer[0].main_layer
        else:
            return None

    def get_geojson_url(self):
        layer = self.get_main_layer()
        url = ""
        if layer != None:
            url = getGeoJsonURLFromLayer(layer)
        return url

    def get_background_layers(self):
        composer = self.composer_community.all()
        if composer:
            return composer[0].composer_layer_community
        else:
            return None

    def not_has_main_layer(self):
        composer = self.composer_community.all()
        if composer:
            return False
        else:
            return True


class MembershipCommunity(idehco3.base.models.Membership):

    community = models.ForeignKey(Community, related_name='membership_list')

    def is_included(self, a_person, a_community):

        try:

            self.__class__.objects.get(member=a_person, community=a_community)

            return True

        except MembershipCommunity.DoesNotExist:

            return False



    def is_not_included(self, a_person, a_community):

        return not self.is_included(
            a_person, a_community)

    def join_us(self, a_person, a_community, an_invite_reason='Join us'):

              self.community = a_community

              self.member = a_person

              self.invite_reason = an_invite_reason

class ComposerCommunity(models.Model):

    headline = models.TextField(null=True, blank=True)
    #banner = image

    community = models.ForeignKey(Community, related_name="composer_community")
    main_layer = models.ForeignKey(Layer, related_name="main_layer")

class ComposerLayer(models.Model):

    checked = models.BooleanField()
    composer_community = models.ForeignKey(ComposerCommunity, related_name="composer_layer_community")
    layer = models.ForeignKey(Layer, related_name="composer_layer_layers")


class Community_Information(modelsGis.Model):

    json_column = JsonBField()  # can pass attributes like null, blank, ecc.
    geom = modelsGis.GeometryField(null=True)









