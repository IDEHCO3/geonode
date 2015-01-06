from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def new_layer(request):
    return render_to_response('layerEditor/new_layer.html',
        RequestContext(request, {}))
