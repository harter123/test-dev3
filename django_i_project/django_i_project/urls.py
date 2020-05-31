"""django_i_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/reports.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    reports. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    reports. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    reports. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from interface_app.views import user_view
from interface_app.views.interface.inerface_detail import InterfaceDetailView
from interface_app.views.interface.interface_list import InterfaceListView
from interface_app.views.service.service_detail import ServiceDetailView
from interface_app.views.service.service_list import ServiceListView
from interface_app.views.task.run_task import get_task_report_list, get_task_report_detail, run_task
from interface_app.views.task.task_detail import TaskDetailView
from interface_app.views.task.task_list import TaskListView
from interface_app.views.task_interface.task_interface_detail import TaskInterfaceDetailView
from interface_app.views.task_interface.task_interface_list import TaskInterfaceListView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/login/', user_view.user_login),
    path('api/user/register/', user_view.user_register),
    path('api/user/logout/', user_view.user_logout),
    path('api/user/info/', user_view.get_user_info),

    path('api/services/', ServiceListView.as_view()),
    path('api/service/<int:base_id>/', ServiceDetailView.as_view()),

    path('api/tasks/', TaskListView.as_view()),
    path('api/task/<int:base_id>/', TaskDetailView.as_view()),

    path('api/interfaces/', InterfaceListView.as_view()),
    path('api/interface/<int:base_id>/', InterfaceDetailView.as_view()),

    path('api/task_interfaces/', TaskInterfaceListView.as_view()),
    path('api/task_interface/<int:base_id>/', TaskInterfaceDetailView.as_view()),

    path('api/task/<int:task_id>/run/', run_task),
    path('api/task/<int:task_id>/reports/', get_task_report_list),
    path('api/task/<int:task_id>/report/<str:report_name>/', get_task_report_detail),
]
