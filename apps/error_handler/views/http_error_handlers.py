# coding:utf-8

from flask import jsonify
from apps.error_handler import error_handlers


@error_handlers.app_errorhandler(404)
def handler_no_found(e):
    result = {"status": -1, "msg":  "this page no found"}
    return jsonify(result), 404
