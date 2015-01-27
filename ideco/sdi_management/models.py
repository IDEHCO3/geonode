from django.db import models

# Create your models here.

class InstanceSDICo(models.Model):

    name = models.CharField(max_length = 150)

    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name
