from django.db import models
import pickle
from cStringIO import StringIO

#from django.contrib.auth.models import AbstractUser
#from django.db.models import signals
#from geonode.people.models import Profile
import geonode
import datetime

# Create your models here.

class Membership(models.Model):

    date_joined = models.DateField(default=datetime.datetime.now())

    is_blocked = models.BooleanField(default=False)

    is_banned = models.BooleanField(default=False)

    invite_reason = models.CharField(max_length=100, null=True, default='Joined us')

    def is_included(self, a_person, an_entity):

        raise NotImplementedError("Please Implement this method")


    def is_not_included(self, a_person, an_entity):

        raise NotImplementedError("Please Implement this method")


    def join_us(self, a_person, an_entity, an_invited_reason):

        raise NotImplementedError("Please Implement this method")


class Invitation(models.Model):

    requested_date = models.DateTimeField(default=datetime.datetime.now())

    expired_date = models.DateTimeField()

    invite_reason = models.CharField(max_length=100, null=True, default='Joined us')

    accepted = models.BooleanField(null=True)

    user_from_ideh_co3 = models.OneToOneField(geonode.settings.AUTH_USER_MODEL, null=True)

    inviter = models.OneToOneField(geonode.settings.AUTH_USER_MODEL, null=False)

    opened = models.BooleanField(null=True, default=False)

class Action(models):

    reiceiver_serialized = models.CharField(null=False)

    message_name = models.CharField(max_length=200, null=False)

    parameter_serialized = models.BigIntegerField(null= False)

    executed = models.BooleanField(null=True)

    def serialize(self, an_object):

        src = StringIO()

        p = pickle.Pickler(src)

        return p.dump(an_object)

    def deserialize(self, serialized_object):

        datastream = src.getvalue()

        dst = StringIO(datastream)

        up = pickle.Unpickler(dst)

        return up.load()









