"""
Create by yy on 2019/9/9
"""
import json

from flask import request, current_app
from tool_yy import debug

from app import redis
from app.api import api
from app.forms.dingyue import ConfigForm
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


@api.route("/get_job", methods=['POST', 'GET'])
def get_job():
    """
    获取配置文件
    :return: json
    """
    operator_code = request.values.get("operator_code", 0)
    if operator_code == 0:
        return Reply.json({
            "data": {},
            "error_code": 1
        })
    # data = current_app.config['GETJOB']
    # data = json.loads(data)
    operator_code = "op_{operator_code}".format(operator_code=operator_code)
    data = redis.get(operator_code)
    if data is None:
        return Reply.json({
            "data": {},
            "error_code": 1
        })
    return Reply.json(data)


@api.route("/config/search_by_code", methods=['GET'])
def search_by_code():
    """
    根据 operator_code 查询数据
    :return:
    """
    operator_code = request.values.get("operator_code", 0)
    if operator_code == 0:
        return Reply.error("failed")
    data = redis.get("op_{operator_code}".format(operator_code=operator_code))
    if data is None:
        return Reply.error("empty")
    return Reply.success([
        {
            "operator_code": operator_code,
            "config": data
        }
    ])


@api.route("/config/add_config", methods=['POST'])
def add_config():
    """
    添加配置
    :return:
    """
    post = request.values
    form = ConfigForm(post)
    if not form.validate():
        return Reply.error(form.errors)
    operator_code = "op_{operator_code}".format(operator_code=form.operator_code.data)
    return Reply.success("ok") if redis.set(operator_code, form.config.data) else Reply.error("failed")


@api.route("/config/update_config", methods=['POST'])
def update_config():
    """
    更新配置
    :return:
    """
    post = request.values
    form = ConfigForm(post)
    if not form.validate():
        return Reply.error(form.errors)
    operator_code = "op_{operator_code}".format(operator_code=form.operator_code.data)
    data = redis.get(operator_code)
    if data is None:
        return Reply.error("此运营商code不存在")
    return Reply.success("ok") if redis.set(operator_code, form.config.data) else Reply.error("failed")


@api.route("/config/login", methods=['POST'])
def login():
    return Reply.success({
        "token": "super_admin"
    })


@api.route("/config/get_info", methods=['GET'])
def get_info():
    return Reply.success("ok")
