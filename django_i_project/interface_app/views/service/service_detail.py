
from interface_app.forms.service_form import ServiceForm
from interface_app.libs.reponse import ErrorCode
from interface_app.models.service import Service
from interface_app.views.base.base_detail import MyBaseDetailView


class ServiceDetailView(MyBaseDetailView):
    model = Service
    form = ServiceForm
    code = ErrorCode.common
