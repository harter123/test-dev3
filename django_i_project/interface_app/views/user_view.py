import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

# Create your views here.
from interface_app.forms.user_form import UserForm
from interface_app.libs.reponse import response_failed, ErrorCode, response_success


@require_http_methods(['POST'])
def user_login(request, *args, **kwargs):
    """
    登录
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    body = request.body
    data = json.loads(body, encoding='utf-8')

    form = UserForm(data)
    if not form.is_valid():
        return response_failed()
    user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
    # username = data.get('username', '')
    # password = data.get('password', '')
    # if not username or not password:
    #     return response_failed()
    # user = authenticate(username=username, password=password)
    if not user:
        return response_failed(code=ErrorCode.auth, message='登录失败')
    else:
        login(request, user)  # 登录持久化
        return response_success()

@require_http_methods(['POST'])
def user_register(request, *args, **kwargs):
    """
    注册
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    body = request.body
    data = json.loads(body, encoding='utf-8')
    # username = data.get('username', '')
    # password = data.get('password', '')
    # if not username or not password:
    #     return response_failed()

    form = UserForm(data)
    if not form.is_valid():
        return response_failed()

    if User.objects.filter(username=form.cleaned_data["username"]).exists():
        return response_failed(code=ErrorCode.auth, message='用户已存在')

    user = User.objects.create_user(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
    if not user:
        return response_failed(code=ErrorCode.auth, message='注册失败')
    else:
        login(request, user)  # 登录持久化
        return response_success()

@require_http_methods(['DELETE'])
def user_logout(request, *args, **kwargs):
    """
    注销
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    logout(request)
    return response_success()

@require_http_methods(['GET'])
def get_user_info(request, *args, **kwargs):
    """
    获取已登录的用户信息
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    user = request.user
    if not user:
        return response_failed(code=ErrorCode.auth, message='用户未登录')
    if user.is_authenticated:  # 判断用户是否已经通过校验
        return response_success(data={
            'id': user.id,
            'name': user.username
        })
    else:
        return response_failed(code=ErrorCode.auth, message='用户未登录')
