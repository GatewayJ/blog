from flask import Blueprint

error_handlers = Blueprint("error_handlers", __name__,url_prefix='error_handler')

from apps.error_handler.views.http_error_handlers import handler_no_found
