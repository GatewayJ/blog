# coding:utf-8

from apps.error_handler import error_handlers


@error_handlers.app_errorhandler(404)
def handler_no_found(e):
    print(e)
    return "this page no found"
