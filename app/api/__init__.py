"""
author songjie
"""
from flask import Blueprint

__all__ = ['api']

api = Blueprint("api", __name__, url_prefix="/api")

from app.api import translate
from app.api import dingyue
from app.api import get_comic_images
