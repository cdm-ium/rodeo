# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py"""
from flask.ext.cache import Cache
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.uuid import FlaskUUID
from flask_migrate import Migrate


# admin = Admin()
cache = Cache()
db = SQLAlchemy()
flask_uuid = FlaskUUID()
migrate = Migrate()
