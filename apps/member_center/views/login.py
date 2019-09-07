# coding:utf-8
from apps.member_center import member_center


@member_center.route('/login')
def hello_world():
    return 'Hello World!'
