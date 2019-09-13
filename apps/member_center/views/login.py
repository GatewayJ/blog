# coding:utf-8
from flask import jsonify, current_app
from apps.member_center import member_center


@member_center.route('/login')
def hello_world():
    result = {"status": 1, "msg": "login ok"}
    return jsonify(result)
