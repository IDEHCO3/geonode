from django.test import TestCase
from ideco.layerEditor import models


import shapefile
# Create your tests here.

class LayerBuilderTestCase(TestCase):

    shp = shapefile.Writer(shapefile.POINT)

    lb = models.LayerBuilder()

    arr_of_field = []

    def setUp(self):

        #create shp attributes
        # create a Character shp attribute.For instance: name Character(30)
        name_shp_char = ('name', 'C', 30, 0)
        self.arr_of_field.append(name_shp_char)
        # create a date shp attribute.For instance: name Character(30)
        name_shp_dt = ('dt', 'D', 0, 0)
        self.arr_of_field.append(name_shp_dt)
        # create a Number shp attribute.For instance: name money(10, 2)
        name_shp_nb1 = ('number_1', 'N', 10, 0)
        self.arr_of_field.append(name_shp_nb1)
        name_shp_nb2 = ('number_2', 'N', 10, 2)
        self.arr_of_field.append(name_shp_nb2)

        self.shp.field(name=name_shp_char[0], type=name_shp_char[1], size=name_shp_char[2], decimal=name_shp_char[3])
        self.shp.field(name=name_shp_dt[0], type=name_shp_dt[1], size=name_shp_dt[2], decimal=name_shp_dt[3])
        self.shp.field(name=name_shp_nb1[0], type=name_shp_nb1[1], size=name_shp_nb1[2], decimal=name_shp_nb1[3])



    def test_create_shape(self):

        shp1 = self.lb.create_shape(name='shp',type=shapefile.POINT, array_of_fields=self.arr_of_field )

        self.assertEqual(self.shp.fields, shp1.fields)