"""
Create by yy on 2019/9/29
"""
from flask import Blueprint

__all__ = ['web']

web = Blueprint("web", __name__, static_folder="../static", static_url_path="/static", template_folder="../template")

from . import dingyue
