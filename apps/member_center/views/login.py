# coding:utf-8
from flask import jsonify, current_app, request
from apps.member_center import member_center
from apps.member_center.models.user import AdminUser
from flask_jwt_extended import create_access_token
from apps import logger, db

from ..forms.AdminUser import AdminUserForm


@member_center.route('/login')
def member_login():
    result = {"status": 1, "msg": "login ok"}
    user_list = AdminUser.query.filter().all()
    return jsonify(result)


@member_center.route('/register', methods=['POST', 'GET'])
def member_register():
    register_json = AdminUserForm()
    logger.info(register_json)
    if register_json.validate_for_api():
        raise TypeError
        if AdminUser.query.filter(AdminUser.user_mail == register_json.user_mail.data).all():
            return jsonify({"register": "fail", "msg": "user_name was exists"})

        admin_user = AdminUser()
        admin_user.user_name = register_json.user_name.data
        admin_user.password = register_json.password.data
        admin_user.user_mail = register_json.user_mail.data
        db.session().add(admin_user)
        db.session().commit()
        access_token = create_access_token(identity=register_json.user_name, fresh=True)

        return jsonify({"register_action": "ok", "access_token":access_token})
    else:
        return jsonify({"register": "fail"})


