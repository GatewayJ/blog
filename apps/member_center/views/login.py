# coding:utf-8
from flask import jsonify, current_app, request
from apps.member_center import member_center
from apps.member_center.models.user import AdminUser
from apps import logger, db

from ..forms.AdminUser import AdminUserForm


@member_center.route('/login')
def member_login():
    result = {"status": 1, "msg": "login ok"}
    user_list = AdminUser.query.filter().all()
    print(user_list)
    return jsonify(result)


@member_center.route('/register')
def member_register():
    register_json = AdminUserForm()
    if register_json.validate_for_api():
        return jsonify({"register_action": "ok"})
    else:
        return jsonify({"register": "fail"})


