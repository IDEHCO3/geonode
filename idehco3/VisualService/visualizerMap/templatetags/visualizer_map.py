from django import template


register = template.Library()

@register.inclusion_tag('visualizerMap/visual_map.html', takes_context=True)
def visual_map(context):
    data = {}
    data['zoom'] = context['zoom']
    data['center_x'] = context['center_longitude']
    data['center_y'] = context['center_latitude']
    data['projection'] = context['projection']

    data['request'] = context['request']
    data['url'] = context['url']
    return data