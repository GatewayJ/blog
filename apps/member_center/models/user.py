# coding:utf-8

from werkzeug.security import generate_password_hash, check_password_hash
from apps import db


class AdminUser(db.Model):
    __tablename__ = 'admin_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    user_name = db.Column(db.String(25), nullable=False, unique=True)
    user_mail = db.Column(db.String(25), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        return AttributeError('this attribute is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password,)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
