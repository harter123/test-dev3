
from interface_app.forms.task_form import TaskInterfaceForm
from interface_app.libs.reponse import ErrorCode
from interface_app.models.task import TaskInterface
from interface_app.views.base.base_detail import MyBaseDetailView


class TaskInterfaceDetailView(MyBaseDetailView):
    model = TaskInterface
    form = TaskInterfaceForm
    code = ErrorCode.task_interface