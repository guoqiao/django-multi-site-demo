from django.contrib import admin
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site
from . import models as m

admin.site.unregister(Site)


class SiteMetaInline(admin.TabularInline):
    model = m.SiteMeta


@admin.register(Site)
class SiteAdminPlus(SiteAdmin):
    inlines = (SiteMetaInline, )

