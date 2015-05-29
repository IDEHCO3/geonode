from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect # Create your views here.
from idehco3.VisualService.layerEditorNew.models import LayerTest

# take the layer from BD, and use the geodjango to do that.
def testEditorLayerNew(request):

    a = LayerTest.objects.all()
    layer = a[20]

    context = {'request': request,
               'layer': layer}
    return render_to_response('layerEditorNew/edit_layer.html',
        RequestContext(request, context))