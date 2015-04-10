from django.db import models
import geonode


class Dashboard(models.Model):

    information = models.CharField(null=True, max_length=100)

    user = models.ForeignKey(geonode.settings.AUTH_USER_MODEL)