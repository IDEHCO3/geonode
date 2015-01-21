from django.db import models

# Create your models here.
from geonode.people.models import Profile


class Community(models.Model):

    name = models.CharField(max_length = 150)

    description = models.TextField(null=True, blank=True)

    usersGeonode = models.ManyToManyField(Profile, null=True, blank=True)

    def users(self):
        return self.usersGeonode.all()

    def __unicode__(self):
        return self.name

    def invite_someone_to_community(self):
        pass

    def invite_user_to_community(self):
        pass

    def manager_community(self):
        pass