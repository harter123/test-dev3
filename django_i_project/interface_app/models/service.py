from django.db import models


# Create your models here.

class Service(models.Model):
    name = models.CharField('名称', blank=False, max_length=200, default="")
    description = models.CharField('描述', blank=False, max_length=2000, default="")
