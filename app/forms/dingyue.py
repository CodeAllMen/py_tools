"""
Create by yy on 2019/9/29
"""
from wtforms import Form, IntegerField, StringField
from wtforms.validators import DataRequired, Length


class ConfigForm(Form):
    operation_code = IntegerField(
        validators=[DataRequired(message="运营商code不能为空，且必须为整数"), Length(min=6, max=6, message="运营商code必须是6位")])
    config = StringField(validators=[DataRequired(message="配置不能为空")])
