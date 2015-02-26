from django.db import models

import shapefile
from subprocess import call
import os
from geonode.layers.utils import upload
# Create your models here.


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

class ShapefileWrite(shapefile.Writer):

    __bbox_temp = []

    marker_type = {'Point': shapefile.POINT, 'Line': shapefile.POLYLINE, 'Polygon': shapefile.POLYGON}

    field_type_dict = {'Character': 'C', 'Number': 'N', 'Date': 'D', 'Logical': 'L'}

    def __init__(self, shapeType='Point', a_bbox_temp=[]):

        shapefile.Writer.__init__(self, self.marker_type[shapeType])

        if (len(a_bbox_temp)==0):
            self.__bbox_temp = self.__bbox_template()
        else:
            self.__bbox_temp = a_bbox_temp



    def __bbox_template(self):
        return [-180, -90, 180, 90]

    def bbox(self):
        """Returns the current bounding box for the shapefile which is
        the lower-left and upper-right corners. It does not contain the
        elevation or measure extremes."""

        if len(self._shapes) == 0:
            return self.__bbox_temp

        else:
            return super.bbox()


class LayerBuilder():

    shp = ShapefileWrite()
    path_file = ""

    def __init__(self, layer_name):
        self.path_file = PROJECT_ROOT+'/temp_shapes/'+layer_name

    def create_shape(self, type_geometry, array_of_field_shp):

        self.shp = ShapefileWrite(type_geometry)

        for field in array_of_field_shp:
            size = field['size']
            decimal = 0
            if field['type'] == 'D':
                size = 8
            if field['type'] == 'L':
                size = 1
            if field.has_key('decimal'):
                decimal = field['decimal']
            self.shp.field(field['name'], field['type'], size, decimal)

        return self.shp

    def __create_projection(self):

        prj = open("%s.prj" % self.path_file, "w")
        epsg = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]]'
        prj.write(epsg)
        prj.close()

    def save_shape(self, shape_in_memory=None, user=None):

        if shape_in_memory is None:
            shape_in_memory = self.shp

        shape_in_memory.save(self.path_file)
        self.__create_projection()

        upload(self.path_file + ".shp", user=user, verbosity=2)

        command_remove_shape = "rm -f "+self.path_file+".*"
        call(command_remove_shape, shell=True)