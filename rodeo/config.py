# -*- coding: utf-8 -*-
from os import path, environ
from distutils.util import strtobool

class BaseConfig(object):

    PROJECT = "rodeo"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = path.abspath(path.dirname(path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    LIST_HISTORY_LIMIT = 50

    ADMINS = ['dino.moraites@globality.com']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = environ.get('RODEO_SECRET', 'secret-key')  # TODO: Change me

    # Fild upload, should override in production.
    # Limited the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


class DefaultConfig(BaseConfig):

    DEBUG = True

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/rodeo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60


class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
