from django.db import models


# Create your models here.

class Task(models.Model):
    name = models.CharField('名称', blank=False, max_length=200, default="")
    description = models.CharField('描述', blank=False, max_length=2000, default="")

class TaskInterface(models.Model):
    task_id = models.IntegerField('任务id', default=0, db_index=True)
    interface_id = models.IntegerField('接口id', default=0)
