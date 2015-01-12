from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
import shapefile as sf

# Create your views here.
def new_layer(request):
    return render_to_response('layerEditor/new_layer.html',
        RequestContext(request, {}))

def create_layer(request):

    marker_type = {'Point': sf.POINT, 'Line': sf.POLYLINE, 'Polygon': sf.POLYGON}
    samples_elements = {'Point': [[[-22,-33]]], 'Line': [[[-22,-33],[-21,-32]]], 'Polygon': [[[-22,-33],[-21,-32],[-22,-32],[-22,-33]]]}

    attributes = request.POST
    layer_name = request.POST["layer_name"]
    layer_type = request.POST["layer_type"]

    if( layer_name == "" ):
        return HttpResponseRedirect(reverse('ledt:new_layer'))

    user_shape = sf.Writer(marker_type[layer_type])
    user_shape.field("id")

    for attribute in attributes:
        if( attributes[attribute] == '' ):
            return HttpResponseRedirect(reverse('ledt:new_layer'))
        if( "attr_name" in attribute ):
            f = attributes[attribute].__getitem__(0)
            f = f.encode("latin_1")
            user_shape.field(f)

    user_shape.poly(parts=samples_elements[layer_type])
    user_shape.record(id='0')
    path_file = '/home/indeco/geonode/downloaded/'+layer_name

    prj = open("%s.prj" % path_file, "w")
    epsg = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]]'
    prj.write(epsg)
    prj.close()

    user_shape.save(path_file)

    return HttpResponseRedirect(reverse('maploom-map-new'))
