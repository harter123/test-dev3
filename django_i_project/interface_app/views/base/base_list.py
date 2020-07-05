import json

from django.forms import model_to_dict
from django.views.generic import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from interface_app.forms.service_form import ServiceForm
from interface_app.libs.reponse import response_success, response_failed, ErrorCode
from interface_app.models.service import Service


class MyBaseListView(View):

    model = Service
    form = ServiceForm
    code = ErrorCode.common

    def get(self, request, *args, **kwargs):
        """
        这个是获取列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        page = request.GET.get('page', 1)
        size = request.GET.get('size', 1000)
        services = self.model.objects.all()
        total = len(services)

        paginator = Paginator(services, size)  # Show 25 contacts per page
        try:
            page_res = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page_res = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page_res = paginator.page(1)

        res = page_res.object_list
        ret = []
        for s in res:
            t = model_to_dict(s)
            ret.append(t)
        return response_success({"page": page, "size": size, "total": total, "list":ret })

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
        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        # service = self.model.objects.create(name=form.cleaned_data["name"], description=form.cleaned_data["description"])
        service = self.model.objects.create(**form.cleaned_data)
        if not service:
            return response_failed(code=self.code, message='创建数据失败')
        else:
            return response_success(model_to_dict(service))
