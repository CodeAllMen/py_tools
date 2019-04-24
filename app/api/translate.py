"""
author songjie
"""
import json

from flask import request, Response

from app.api import api
from app.api.models.translate import Translate


@api.route("/translate")
def translate():
    response_data = dict()
    try:
        content = request.values.get("content")
        src = request.values.get("src")
        dest = request.values.get("dest")
        response_data["data"] = Translate().translate(content, src, dest)
        response_data["code"] = 0
        response_data["status"] = 200
    except Exception as e:
        response_data["data"] = str(e)
        response_data["code"] = 1
        response_data["status"] = 500
    return Response(json.dumps(response_data), mimetype="application/json;charset=utf-8")
