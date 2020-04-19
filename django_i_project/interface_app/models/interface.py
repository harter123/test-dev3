from django.db import models


# Create your models here.

class Interface(models.Model):
    name = models.CharField('名称', blank=False, max_length=200, default="")
    description = models.CharField('描述', blank=False, max_length=2000, default="")
    service_id = models.IntegerField('service的id', default=0)
    context = models.CharField('内容', blank=False, max_length=4000, default="{}")
    # 这个就是json的转成字符串
    # 这里包括 method, url, 参数，断言
    # {
    #     "method": "get",
    #     "url": "",
    #     "params": {},
    #     "assert": {}
    # }