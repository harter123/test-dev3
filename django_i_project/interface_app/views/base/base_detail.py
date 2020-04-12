import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_app.forms.service_form import ServiceForm
from interface_app.libs.reponse import ErrorCode, response_failed, response_success
from interface_app.models.service import Service


class MyBaseDetailView(View):
    model = Service
    form = ServiceForm
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
        return response_success(model_to_dict(service))

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
        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        service = self.model.objects.filter(id=base_id).first()
        if not service:
            return response_failed(code=self.code, message='数据不存在')

        # service = self.model.objects.filter(id=service_id).update(name=form.cleaned_data["name"], description=form.cleaned_data["description"])
        self.model.objects.filter(id=base_id).update(**form.cleaned_data) # 这里返回的id
        service = self.model.objects.filter(id=base_id).first()
        return response_success(model_to_dict(service))

    def patch(self, request, base_id, *args, **kwargs):
        """
        这个是部分修改数据
        :param request:
        :param base_id:
        :param args:
        :param kwargs:
        :return:
        """
        return self.put(request, base_id, *args, **kwargs)

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
