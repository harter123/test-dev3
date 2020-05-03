import json

from django.forms import model_to_dict

from interface_app.forms.interface_form import InterfaceForm
from interface_app.libs.reponse import ErrorCode, response_success, response_failed
from interface_app.models.interface import Interface
from interface_app.views.base.base_list import MyBaseListView


class InterfaceListView(MyBaseListView):
    model = Interface
    form = InterfaceForm
    code = ErrorCode.common

    def get(self, request, *args, **kwargs):
        """
        这个是获取某个的服务下的接口列表，get方法是怎么传的
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        service_id = request.GET.get('service_id', 0) # 0代表默认值
        interfaces = self.model.objects.filter(service_id=service_id)
        ret = []
        for s in interfaces:
            # t = dict()
            # t['id'] = s.id
            # t['name'] = s.name
            # t['description'] = s.description
            # t['service_id'] = s.service_id
            # t['context'] = json.loads(s.context, encoding="utf-8") # 把字符串改为字典传到前端
            t = model_to_dict(s)
            t['context'] = json.loads(t['context'], encoding="utf-8")
            ret.append(t)
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        这个是创建数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        data = json.loads(body, encoding='utf-8')
        if "context" not in data:
            return response_failed()

        data['context'] = json.dumps(data['context'])
        print(data)
        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        service = self.model.objects.create(**form.cleaned_data)
        if not service:
            return response_failed(code=self.code, message='创建数据失败')
        else:
            ret = model_to_dict(service)
            ret['context'] = json.loads(ret['context'], encoding="utf-8")
            return response_success(ret)
