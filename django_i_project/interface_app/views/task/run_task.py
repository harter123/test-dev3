import datetime
import os
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from interface_app.models.task import RunTask


def _create_task_report_dir(task_id):
    task_reports_path = os.path.join(settings.BASE_DIR, "task_test", "reports", str(task_id))
    if os.path.exists(task_reports_path):
        return
    os.makedirs(task_reports_path)


def _add_task_to_run_modal(task_id):
    RunTask.objects.all().delete()
    RunTask.objects.create(task_id=task_id)


def _run_py_test(task_id):
    now = datetime.datetime.now()
    run_task_path = os.path.join(settings.BASE_DIR, "task_test", "run_task.py")
    report_name = now.strftime("%Y-%m-%d-%H-%M-%S") + ".html"
    report_path = os.path.join(settings.BASE_DIR, "task_test", "reports", str(task_id), report_name)
    command = "pytest " + run_task_path + " --html=" + report_path
    os.system(command)


@require_http_methods(['GET'])
def run_task(request, task_id):  # 执行任务
    _create_task_report_dir(task_id)  # 1. 创建目录
    _add_task_to_run_modal(task_id)  # 2. 把任务id添加到执行表里面去
    _run_py_test(task_id)  # 3. 执行pytest
    return HttpResponse()


@require_http_methods(['GET'])
def get_task_report_list(request, task_id):  # 获取任务的report列表
    return HttpResponse()


@require_http_methods(['GET'])
def get_task_report_detail(request, task_id, report_name):  # 获取任务的某个report
    return HttpResponse()
