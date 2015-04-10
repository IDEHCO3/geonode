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

    can_edit = models.BooleanField(default=True)

    can_invite = models.BooleanField(default=True)

    invite_reason = models.CharField(max_length=300, null=True, default='Joined us')

    member = models.ForeignKey(geonode.settings.AUTH_USER_MODEL, db_column='member_id')


    def is_included(self, a_person, an_entity):

        raise NotImplementedError("Please Implement this method")


    def is_not_included(self, a_person, an_entity):

        raise NotImplementedError("Please Implement this method")


    def join_us(self, a_person, an_entity, an_invited_reason):

        raise NotImplementedError("Please Implement this method")

    def is_owner(self):

        return self.owner is not None


class Action(models.Model):

    receiver_serialized = models.CharField(null=False, max_length=10000)

    message_name = models.CharField(max_length=200, null=False)

    parameter_serialized = models.CharField(null= False, max_length=10000)

    executed = models.NullBooleanField(null=True)


    def receiver_message_parameter(self,receiver, message, parameter):

        self.receiver_serialized = self.serialize(receiver)

        self.message_name = message

        self.parameter_serialized = self.serialize(parameter)


    def serialize(self, an_object):

        src = StringIO()

        p = pickle.Pickler(src)

        p.dump(an_object)

        dataStream = src.getvalue()

        return dataStream


    def deserialize(self, serialized_object):

        dst = StringIO(serialized_object)

        up = pickle.Unpickler(dst)

        return up.load()


    def execute(self):

        self.executed = True

        receiver_object = self.deserialize(self.receiver_serialized)


        parameter_object = self.deserialize(self.parameter_serialized)


        if self.parameter_serialized is None:

            return getattr(receiver_object, self.message_name)()

        arr = []

        arr.append(parameter_object)


        return getattr(receiver_object, self.message_name)(*arr)


class Invitation(models.Model):

    requested_date = models.DateTimeField(default=datetime.datetime.now())

    expired_date = models.DateTimeField(null=True)

    invite_reason = models.CharField(max_length=100, null=True, default='Joined us')

    accepted = models.NullBooleanField(null=True)

    invited = models.ForeignKey(geonode.settings.AUTH_USER_MODEL, null=True, related_name= 'invitations')

    inviter = models.OneToOneField(geonode.settings.AUTH_USER_MODEL, null=False)

    opened = models.NullBooleanField(null=True, default=False)

    action = models.OneToOneField(Action, null=True)

    def accept(self):

        return self.action.execute()












