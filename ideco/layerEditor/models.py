from django.db import models
import shapefile

# Create your models here.

class ShapefileWrite(shapefile.Writer):

    __bbox_temp = []

    def __init__(self, shapeType=None, a_bbox_temp=[]):

        shapefile.Writer.__init__(self, shapeType)

        if (len(a_bbox_temp)==0):
            self.__bbox_temp = self.__bbox_template()
        else:
            self.__bbox_temp = a_bbox_temp



    def __bbox_template(self):
        return [-180,-90, 180,90]

    def bbox(self):
        """Returns the current bounding box for the shapefile which is
        the lower-left and upper-right corners. It does not contain the
        elevation or measure extremes."""

        if len(self._shapes) == 0:
            return self.__bbox_temp

        else:
            return super.bbox()

"""
class LayerBuilder():

    def __init__(self, name, layer_type, array_tuples):

    marker_type = {'Point': shapefile.POINT, 'Line': shapefile.POLYLINE, 'Polygon': shapefile.POLYGON}

    field_type_dict = {'Character': 'C', 'Number': 'N', 'Date': 'D', 'Long': 'L'}

    samples_elements = {'Point': [[[-43.2096, -22.9035]]],
                        'Line': [[[-43.2096, -22.9035], [-43.1996, -22.8935]]],
                        'Polygon': [[[-43.2096, -22.9035], [-43.1996, -22.8935], [-43.2096, -22.8935], [-43.2096, -22.9035]]]}


    def create_shape(self, name, type_geometry, array_of_field_shp):

        shp = shapefile.Writer(self.marker_type[type_geometry])

        for field in array_of_field_shp:

            shp.field(field[0],field[1], field[2], field[3])

        return shp


    def createLayer(self, layerDictionary, attributesDictionary, userOwner):



        for attributeDict in attributesDictionary:
            shape.field()


        return Layer()

    def createAttribute(self):
        return

    def create_layer(request):


    for attribute in attributes:
        if( attributes[attribute] == '' ):
            return HttpResponseRedirect(reverse('ledt:new_layer'))
        if( "attr_name" in attribute ):
            f = attributes[attribute]
            f = f.encode("latin_1")
            user_shape.field(f)

    user_shape.poly(parts=samples_elements[layer_type])
    user_shape.record(id='0')
    path_file = PROJECT_ROOT+'/temp_shapes/'+layer_name

    prj = open("%s.prj" % path_file, "w")
    epsg = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]]'
    prj.write(epsg)
    prj.close()

    user_shape.save(path_file)

    upload(path_file + ".shp", user=request.user, verbosity=2)

    command_remove_shape = "rm -f "+path_file+".*"
    call(command_remove_shape, shell=True)

    arguments = "?layer=geonode:"+layer_name
    arguments = arguments.encode("latin_1")

"""