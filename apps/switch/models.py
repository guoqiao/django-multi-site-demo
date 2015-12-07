from django.db import models
from django.contrib.sites.models import Site


class SiteMeta(models.Model):
    site = models.ForeignKey(Site)
    key = models.SlugField(max_length=30)
    value = models.TextField()
