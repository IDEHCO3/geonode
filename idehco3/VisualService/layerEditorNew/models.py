from django.contrib.gis.db import models

# Create your models here.
class LayerTest(models.Model):

    pk = models.IntegerField(name='gid', primary_key=True)
    name = models.CharField(name='name', max_length=50)
    geom = models.MultiPolygonField(name='geom')
    objects = models.GeoManager()

    class Meta():
        db_table = 'tm_world_borders-0.3'
