"""
author songjie
"""
from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api")

from app.api import translate
from app.api import dingyue
