"""
author songjie
"""
from flask import Flask
from redis_yy import RedisDB

__all__ = ['create_app', 'redis']

redis = RedisDB()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings")
    app.config.from_object("config.secure")
    app.config.from_object("config.pin")
    redis.init_helper(app)
    app.redis.init()
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.api import api
    app.register_blueprint(api)
