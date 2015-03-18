# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_list_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext

from idehco3.knowledgeManagement.models import Knowledge, Frequencia
from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode.people.models import Profile


def index(request):
    latest_knowledge_list = Knowledge.objects.all().order_by('-pub_date')
    return render_to_response('knowledgeManagement/index.html',
        RequestContext(request, {'latest_knowledge_list': latest_knowledge_list}))

def detail(request, knowledge_id):
    try:
        k = Knowledge.objects.get(pk=knowledge_id)
    except Knowledge.DoesNotExist:
        raise Http404
    return render_to_response('knowledgeManagement/detail.html',
                              {'knowledge': k},
                              context_instance=RequestContext(request))

def getMapKnowledge(request, map_id):
    k_list = get_list_or_404(Knowledge.objects.filter(mapa = map_id).order_by('-pub_date'))
    return render_to_response ('knowledgeManagement/get_map_knowledge.html', 
                                {'knowledge_list' : k_list},
                                context_instance=RequestContext(request))

def getLayerKnowledge(request, layer_id):
    k_list = get_list_or_404(Knowledge.objects.filter(camada = layer_id).order_by('-pub_date'))
    return render_to_response ('knowledgeManagement/get_layer_knowledge.html', 
                                {'knowledge_list' : k_list},
                                context_instance=RequestContext(request))

def putKnowledge(request):
    resposta = {'destino' : 'layer_detail', 'nome' : ''}
    if (request.POST['objTipo'] == 'camada'):
        k = Knowledge(usuario = Profile.objects.get(pk = request.POST['userID']),
                      camada = Layer.objects.get(pk = request.POST['objID']),
                      frequencia = Frequencia.objects.get(pk = request.POST['frequencia']),
                      whatFor = request.POST['whatFor'],
                      desirable_scale = request.POST['desirable_scale'],
                      missing_information = request.POST['missing_information'],
                      resolution = request.POST['resolution'])
        resposta = {'destino' : 'layer_detail', 'nome' : 'geonode:' + k.camada.name}
        k.save()       

    elif (request.POST['objTipo'] == 'mapa'):
        k = Knowledge(usuario = Profile.objects.get(pk = request.POST['userID']),
                      mapa = Map.objects.get(pk = request.POST['objID']),
                      frequencia = Frequencia.objects.get(pk = request.POST['frequencia']),
                      whatFor = request.POST['whatFor'],
                      desirable_scale = request.POST['desirable_scale'],
                      missing_information = request.POST['missing_information'],
                      resolution = request.POST['resolution'])
        resposta = {'destino' : 'map_detail', 'nome' : str(k.mapa.id)}
        k.save() 
    
    return HttpResponseRedirect(reverse(resposta['destino'], args = (resposta['nome'],)))