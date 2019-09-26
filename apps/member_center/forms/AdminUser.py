# coding:utf-8

from apps.common_utils import form_base
from wtforms import StringField
from wtforms.validators import DataRequired,Length


class AdminUserForm(form_base.JsonBaseForm):
    user_name = StringField(validators=[DataRequired(), Length(1, 25)])
    user_mail = StringField(validators=[DataRequired(), Length(1, 25)])
    password = StringField(validators=[DataRequired(), Length(1, 255)])
