from django.http import JsonResponse


class ErrorCode:
    common = 10000
    auth = 10001
    service = 10002
    task = 10003
    task_interface = 10003


# 这是一个通用的
def common_response(success, data, error_code, error_message):
    response = {
        "data": data,
        "success": success, #布尔型，成功或者是失败的标志
        "error": {
            "code": error_code,  # 错误码
            "message": error_message
        }
    }
    return JsonResponse(response, safe=False)


# 这两个是快捷方式
def response_success(data={}):
    return common_response(True, data, "", "")


def response_failed(code=ErrorCode.common, message="参数错误", data={}):
    return common_response(False, data, code, message)
