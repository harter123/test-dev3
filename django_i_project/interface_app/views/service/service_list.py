from django.views.generic import View


class ServiceListView(View):

    def get(self, request, *args, **kwargs):
        """
        这个是获取列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def post(self, request, *args, **kwargs):
        """
        这个是创建数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass
