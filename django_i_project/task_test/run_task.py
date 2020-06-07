# -*- coding: UTF-8 –*-
import pytest
import os
import sys
import django
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 定位到你的django根目录
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))  # 把django目录放到环境变量里面
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_i_project.settings")  # django项目的配置，你的django的settings文件
django.setup()  # django的初始化

from interface_app.models.task import TaskInterface, RunTask
from interface_app.models.interface import Interface
from task_test.http_request import HttpRequest

run_task = RunTask.objects.all().first()  # 1. 提供一个任务id
if run_task is None:
    exit(-1)
task_id = run_task.task_id

params_list = []  # 这是参数列表

 # reports. 获取任务所有的接口
task_i_s = TaskInterface.objects.filter(task_id=task_id)
for item in task_i_s:
    interface = Interface.objects.filter(id=item.interface_id).first()
    context = json.loads(interface.context, encoding="utf-8")
    item_data = [
        interface.name,
        context.get('method', ""),
        context.get('url', ""),
        context.get('params', {}),
        context.get('assert', {}),
    ]
    params_list.append(item_data)  # 3. 这是构造参数化列表

@pytest.mark.parametrize(("name", "method", "url", "params", "assertions"), params_list)
def test_task(name, method, url, params, assertions):
    response = HttpRequest.send_request(url, method, params)  # 4. 进行http请求，获取响应

    for text in assertions:  # 5. 进行断言
        rule = assertions[text]
        if rule == "include":
            assert str(text) in str(response)
        elif rule == "exclude":
            assert str(text) not in str(response)
        else:
            continue