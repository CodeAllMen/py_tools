"""
Create by yy on 2019/9/9
"""
import json

from flask import request, current_app

from app import redis
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


@api.route("/get_job", methods=['POST', 'GET'])
def get_job():
    """
    获取配置文件
    :return: json
    """
    data = current_app.config['GETJOB']
    data = json.loads(data)
    return Reply.json(data)


@api.route("/config/search_by_code", methods=['GET'])
def search_by_code():
    operation_code = request.values.get("operation_code", 0)
    if operation_code == 0:
        return Reply.error("failed")
    data = redis.get(operation_code)
    if data is None:
        return Reply.error("empty")
    return Reply.success({
        "operation_code": operation_code,
        "config": data
    })
