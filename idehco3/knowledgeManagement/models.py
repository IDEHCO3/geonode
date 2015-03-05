# -*- coding: utf-8 -*-
from django.db import models
from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode.people.models import Profile
from datetime import datetime 

class Frequencia(models.Model):
    frequencia = models.CharField(max_length=100)
    def __unicode__(self):
        return self.frequencia

class Knowledge(models.Model):
    camada = models.ForeignKey(Layer, blank=True, null=True, on_delete=models.SET_NULL)
    mapa = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    frequencia = models.ForeignKey(Frequencia)
    pub_date = models.DateTimeField(u'Publicação', default=datetime.now)
    whatFor = models.CharField(max_length = 200)

    desirable_scale = models.CharField(max_length = 200)
    status = models.CharField(max_length = 1)
    missing_information = models.TextField(null=True, blank=True)
    resolution = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.whatFor

    def get_absolute_url(self):
        return self.usuario.get_absolute_url()