"""
Create by yy on 2020/2/17
"""
from flask import Response, request
from tool_yy import curl_data

from app.api import api


@api.route("/get_comic_image")
def get_comic_image():
    url = request.values.get("url")
    data = curl_data(url, open_virtual_ip=True)
    return Response(data, mimetype="image/jpeg")
