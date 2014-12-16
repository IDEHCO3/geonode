from django import template

from knowledgeManagement.models import Knowledge, Frequencia

register = template.Library()

@register.inclusion_tag('knowledgeManagement/_in_knowledge.html', takes_context = True)
def mapKnowledgeTag(context):
    k_list = Knowledge.objects.filter(mapa = context['resource']).order_by('-pub_date')[:5]
    f_list = Frequencia.objects.all().order_by('-id')    
    if k_list.count() > 0:    
        retorno = {'conhecimentos' : k_list,
                   'frequencias' : f_list,
                   'tipo' : 'mapa',
                   'objID' : context['resource'].id,
                   "request":context['request']}
    else:
        retorno = {'frequencias' : f_list,
                   'tipo' : 'mapa',
                   'objID' : context['resource'].id,
                   "request":context['request']}
   
    
    return retorno


@register.inclusion_tag('knowledgeManagement/_in_knowledge.html', takes_context = True)
def layerKnowledgeTag(context):
    k_list = Knowledge.objects.filter(camada = context['resource']).order_by('-pub_date')[:5]
    f_list = Frequencia.objects.all().order_by('-id')
    if k_list.count() > 0:    
        retorno = {'conhecimentos' : k_list,
                   'frequencias' : f_list,
                   'tipo' : 'camada',
                    'objID' : context['resource'].id,
                    "request":context['request']}
    else:
        retorno = {'frequencias' : f_list,
                   'tipo' : 'camada',
                    'objID' : context['resource'].id,
                    "request":context['request']}
    return retorno