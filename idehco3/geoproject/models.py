import datetime
from django.db import models

# Create your models here.
import geonode
from geonode import settings
import idehco3

from idehco3.base.models import Membership

class Project(models.Model):

    name = models.CharField(max_length = 150)

    description = models.TextField(null=True, blank=True)

    start_date = models.DateTimeField(default=datetime.datetime.now())

    onwer = models.OneToOneField(geonode.settings.AUTH_USER_MODEL, null=False)


    def __unicode__(self):
        return self.name


class TypeOfProject(models.Model):

    name = models.CharField(max_length = 150)

    description = models.CharField(max_length=500, null=True, blank=True)


class MembershipProject(idehco3.base.models.Membership):

    project = models.ForeignKey(Project, related_name='membership_list')

    def is_included(self, a_person, a_project):

        try:

            self.__class__.objects.get(member=a_person, project=a_project)

            return True

        except MembershipProject.DoesNotExist:

            return False


