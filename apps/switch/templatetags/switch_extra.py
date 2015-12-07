from django.template import Library
from django.template.defaultfilters import stringfilter
from .. import models as m

register = Library()

################ Filters
@register.filter
def filter_with_arg(value, arg):
    return value

@register.filter
@stringfilter
def string_filter(s):
    return s

################ Tags
@register.simple_tag()
def simple_tag(arg1, arg2, arg3):
    return ''

@register.simple_tag(takes_context=True)
def site_meta(context, key):
    site = context['site']
    meta = m.SiteMeta.objects.get(site=site, key=key)
    return meta.value

@register.inclusion_tag('path/to/template.html')
def sidebar(obj):
    return {'obj': obj}
