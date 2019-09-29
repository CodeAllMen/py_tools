"""
Create by yy on 2019/9/29
"""
from flask import render_template

from app.libs.reply import Reply
from app.web import web


@web.route("/set_config")
def set_config():
    title = "添加配置文件"
    return render_template("dingyue/set_config.html", title=title)
