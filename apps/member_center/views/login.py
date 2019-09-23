# coding:utf-8
from flask import jsonify, current_app
from apps.member_center import member_center
from apps.member_center.models.user import AdminUser
from apps import logger, db


@member_center.route('/login')
def hello_world():
    result = {"status": 1, "msg": "login ok"}
    user_list = AdminUser.query.filter().all()
    print(user_list)
    return jsonify(result)
