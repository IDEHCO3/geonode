from django import template


register = template.Library()

@register.inclusion_tag('visualizerMap/visual_map.html', takes_context=True)
def visual_map(context):
    retorno = {}
    #retorno['urlData'] = context['urlData'] #url of json data
    retorno['zoom'] = context['zoom']
    retorno['center_x'] = context['center_longitude']
    retorno['center_y'] = context['center_latitude']
    retorno['projection'] = context['projection']

    retorno['request'] = context['request']
    retorno['geoJsonURL'] = context['geoJsonURL']
    return retorno