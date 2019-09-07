from flask import Blueprint

member_center = Blueprint("member_center", __name__, url_prefix='/member_center')

from apps.member_center.views import login
