# coding:utf-8

from flask import request
from wtforms import Form
from apps.error_handler.views.http_error_handlers import ParameterException


# Json 基础验证器
class JsonBaseForm(Form):
    # 接收Jason参数
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(JsonBaseForm, self).__init__(data=data, **args)

    # 对验证错误的参数抛出异常
    def validate_for_api(self):
        valid = super(JsonBaseForm, self).validate()
        if not valid:
            # form errors
            print("f")
            raise ParameterException()
        return self
