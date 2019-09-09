"""
Create by yy on 2019/9/9
"""
from flask import request, current_app

from app.api import api
from app.libs.reply import Reply


@api.route("/check_is_pin")
def check_is_pin():
    """
    此接口用于
    根据传过来的code
    判断是否有pin码
    :return:
    """
    operator = request.values.get("operator", 0)
    if operator == 0:
        return Reply.error("参数传递出错")
    if str(operator) in current_app.config['PIN']:
        return Reply.success(current_app.config['PIN'][str(operator)])
    return Reply.error("无此 code， 请添加对应的code和类型")