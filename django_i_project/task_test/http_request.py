# -*- coding: UTF-8 –*-
import requests
import traceback

class HttpRequest:

    @classmethod
    def assert_response(cls, assertions, response):
        """
        # 断言格式:
    # {
    #
    #          "a": "include",
     #         "b": "exclude",
    #
    # }
        :param assertions:
        :param response:
        :return:
        """
        for text in assertions:
            rule =assertions[text]
            if not rule:
                continue
            if rule == "include":
                assert str(text) in str(response)
            elif rule == "exclude":
                assert str(text) not in str(response)
            else:
                continue
        return

    @classmethod
    def send_request(cls, url, method, params):
        if not url or not method:
            return ""
        ret = ''
        try:
            if "GET" == method or "get" == method:
                ret = cls._get_request(url, params)
            elif "POST" == method or "post" == method:
                ret = cls._post_request(url, params)
            elif "DELETE" == method or "delete" == method:
                ret = cls._delete_request(url, params)
            elif "PUT" == method or "put" == method:
                ret = cls._put_request(url, params)
            return ret
        except Exception:
            return traceback.format_exc()

    @classmethod
    def _get_request(cls, url, parameter):
        """
        get请求，数据都在url，超时30s
        :param url: 字符串
        :param parameter: 字典
        :return:
        """
        ret = requests.get(url, params=parameter, timeout=30)
        ret.encoding = 'utf-8'
        return ret.text

    @classmethod
    def _post_request(cls, url, parameter):
        """
        post 请求
        :param url:
        :param parameter: 字典
        :return:
        """
        header = {
            "content-type": "application/json"
        }
        ret = requests.post(url, json=parameter, headers=header, timeout=30)
        ret.encoding = 'utf-8'
        return ret.text

    @classmethod
    def _delete_request(cls, url, parameter):
        """
        delete请求
        :param url:
        :param parameter:
        :return:
        """
        header = {
            "content-type": "application/json"
        }
        ret = requests.delete(url, json=parameter, headers=header, timeout=30)
        ret.encoding = 'utf-8'
        return ret.text

    @classmethod
    def _put_request(cls, url, parameter):
        """
        put请求
        :param url:
        :param parameter:
        :return:
        """
        header = {
            "content-type": "application/json"
        }
        ret = requests.put(url, json=parameter, headers=header, timeout=30)
        ret.encoding = 'utf-8'
        return ret.text