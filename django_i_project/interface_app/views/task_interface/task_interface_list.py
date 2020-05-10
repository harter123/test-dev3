import json

from django.forms import model_to_dict

from interface_app.forms.task_form import TaskInterfaceForm
from interface_app.libs.reponse import ErrorCode, response_success, response_failed
from interface_app.models.interface import Interface
from interface_app.models.task import TaskInterface
from interface_app.views.base.base_list import MyBaseListView


class TaskInterfaceListView(MyBaseListView):
    model = TaskInterface
    form = TaskInterfaceForm
    code = ErrorCode.task_interface

    def get(self, request, *args, **kwargs):
        """
        这个是获取列表, 需要一个参数：task_id 在url里面
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        task_id = request.GET.get('task_id', 0)

        task_interfaces = TaskInterface.objects.filter(task_id=task_id)  # 拿到任务所有的接口
        ret = []
        for s in task_interfaces:
            interface = Interface.objects.filter(id=s.interface_id).first()
            t = model_to_dict(interface)
            t['context'] = json.loads(t['context'], encoding="utf-8")
            t['task_id'] = task_id
            t['task_interface_id'] = s.id
            ret.append(t)
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        这个是创建数据, 我们需要处理一下，因为我们是批量添加
        所以我们的要求的参数就变成了一个列表：

        [{task_id:1, interface_id:1}, {task_id:1, interface_id:1}, {task_id:1, interface_id:1}]
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        data = json.loads(body, encoding='utf-8')

        # 数组参数校验,是否是数组
        if not isinstance(data, list):
            return response_failed()

        for item in data:
            form = self.form(item)
            if not form.is_valid():
                return response_failed()

            service = self.model.objects.create(**form.cleaned_data)
            if not service:
                return response_failed(code=self.code, message='创建数据失败')

        return response_success()
