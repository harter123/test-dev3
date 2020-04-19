import json

from django.forms import model_to_dict

from interface_app.forms.interface_form import InterfaceForm
from interface_app.libs.reponse import ErrorCode, response_failed, response_success
from interface_app.models.interface import Interface
from interface_app.views.base.base_detail import MyBaseDetailView


class InterfaceDetailView(MyBaseDetailView):
    model = Interface
    form = InterfaceForm
    code = ErrorCode.common

    def get(self, request, base_id, *args, **kwargs):
        """
        这个是单个数据
        :param request:
        :param base_id:
        :param args:
        :param kwargs:
        :return:
        """
        service = self.model.objects.filter(id=base_id).first()
        if not service:
            return response_failed(code=self.code, message='数据不存在')
        ret = model_to_dict(service)
        ret['context'] = json.loads(ret['context'], encoding="utf-8")
        return response_success(ret)

    def put(self, request, base_id, *args, **kwargs):
        """
        这个是全量修改数据
        :param request:
        :param base_id:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        data = json.loads(body, encoding='utf-8')

        if "context" not in data:
            return response_failed()
        data['context'] = json.dumps(data['context'], encoding='utf-8')

        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        service = self.model.objects.filter(id=base_id).first()
        if not service:
            return response_failed(code=self.code, message='数据不存在')

        self.model.objects.filter(id=base_id).update(**form.cleaned_data) # 这里返回的id
        service = self.model.objects.filter(id=base_id).first()
        return response_success(model_to_dict(service))

    def delete(self, request, base_id, *args, **kwargs):
        """
        这个是删除数据
        :param request:
        :param base_id:
        :param args:
        :param kwargs:
        :return:
        """
        self.model.objects.filter(id=base_id).delete()
        return response_success()
