
from interface_app.forms.task_form import TaskForm
from interface_app.libs.reponse import ErrorCode
from interface_app.models.task import Task
from interface_app.views.base.base_detail import MyBaseDetailView


class TaskDetailView(MyBaseDetailView):
    model = Task
    form = TaskForm
    code = ErrorCode.task