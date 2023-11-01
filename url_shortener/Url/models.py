from django.db import models

# Create your models here.

class Urls(models.Model):

    long_url = models.URLField(null=False, blank=False, unique=True)
    short_url = models.CharField(null=False, blank=False, max_length=10, unique=True)