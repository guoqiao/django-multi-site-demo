from django.contrib.sites.models import Site

site = Site.objects.get_current()

def g(request):
    ctx = {}
    ctx['site'] = site
    return ctx
