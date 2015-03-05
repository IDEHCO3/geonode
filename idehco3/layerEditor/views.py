from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from geonode.people.models import Profile

import json
import shapefile as sf
from idehco3.layerEditor.models import LayerBuilder, ShapefileWrite
from subprocess import call
import os
from geonode.layers.utils import upload

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Create your views here.
def new_layer(request):
    return render_to_response('layerEditor/new_layer.html',
        RequestContext(request, {"request": request}))

def create_layer(request):

    layer_name = request.POST["layer_name"]
    layer_type = request.POST["layer_type"]

    if layer_name == "":
        return HttpResponseRedirect(reverse('layerEditor:new_layer'))

    attributes = getAttributesFromRequest(request)

    layer = LayerBuilder(layer_name)

    shape = layer.create_shape(layer_type, attributes)
    layer.save_shape(shape_in_memory=shape, user=request.user)

    arguments = "?layer=geonode:"+layer_name.lower()
    arguments = arguments.encode("latin_1")

    return HttpResponseRedirect(reverse('new_map') + arguments)

def getAttributesFromRequest(request):
    number_of_attributes = int(request.POST["number_attributes"])

    attributes = []

    for attr in range(0, number_of_attributes):
        attributes.append({})

    for attribute in request.POST:
        if request.POST[attribute] == '':
            continue
        if "attr_name" in attribute:
            position = int(attribute[9:])
            name = request.POST[attribute]
            name = name.encode("latin_1")
            attributes[position]["name"] = name

        if "attr_type" in attribute:
            position = int(attribute[9:])
            attributes[position]['type'] = ShapefileWrite.field_type_dict[request.POST[attribute]]

        if "attr_size" in attribute:
            position = int(attribute[9:])
            attributes[position]['size'] = int(request.POST[attribute])

        if "attr_decimal" in attribute:
            position = int(attribute[12:])
            attributes[position]['decimal'] = int(request.POST[attribute])

    return attributes
