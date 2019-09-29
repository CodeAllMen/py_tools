"""
author songjie
"""
from flask import Flask
from flask_cors import CORS
from redis_yy import RedisDB

from app.errors import register_error

__all__ = ['create_app', 'redis']

redis = RedisDB()


def create_app():
    app = Flask(__name__, template_folder="./template")
    app.config.from_object("config.settings")
    app.config.from_object("config.secure")
    app.config.from_object("config.pin")
    redis.init_helper(app)
    app.redis.init()
    register_blueprint(app)
    register_error(app)
    CORS(app, supports_credentials=True)
    return app


def register_blueprint(app):
    from app.api import api
    app.register_blueprint(api)
    from app.web import web
    app.register_blueprint(web)
