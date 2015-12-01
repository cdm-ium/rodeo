"""The app module, containing the app factory function."""
from logging import error, ERROR, INFO
from logging import Formatter, StreamHandler
from logging.handlers import SMTPHandler
from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

from rodeo.api.v1 import picture_api as picture_api_v1
from rodeo.config import DefaultConfig, TestConfig
from rodeo.extensions import cache, db, flask_uuid, migrate


__all__ = ['create_app']

# Default Flask Blueprints to load unless specified otherwise in runtime
DEFAULT_BLUEPRINTS = [
    picture_api_v1
]


def create_app(config=None, app_name=None, blueprints=None, testing=False):
    """Create a Flask app."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    if testing:
        config = TestConfig

    app = Flask(app_name)

    configure_app(app, config)
    configure_hook(app)
    # Extensions should be configured before blueprints in order for
    # custom URL converters to be available to all Blueprints.
    configure_extensions(app)
    configure_blueprints(app, blueprints)
    configure_logging(app)
    configure_error_handlers(app)
    configure_services(app, testing=testing)

    return app


def configure_app(app, config=None):
    """Different ways of configurations."""
    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    if config:
        app.config.from_object(config)

    app.config.from_envvar('{}_SETTINGS'.format(DefaultConfig.PROJECT.upper()), silent=True)


def configure_extensions(app):
    """Configure Flask app extensions e.g SQLAlchemy, Cache."""
    # flask-sqlalchemy
    db.init_app(app)

    # flask-cache
    cache.init_app(app)

    # flask-migrate
    migrate.init_app(app, db)

    # flask-uuid
    flask_uuid.init_app(app)


def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_logging(app):
    """Configure file(info) and email(error) logging."""
    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return

    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(INFO)

    info_file_handler = StreamHandler()
    info_file_handler.setLevel(INFO)
    info_file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)

    # Testing
    # app.logger.info("testing info.")
    # app.logger.warn("testing warn.")
    # app.logger.error("testing error.")

    mail_handler = SMTPHandler(app.config['MAIL_SERVER'],
                               app.config['MAIL_USERNAME'],
                               app.config['ADMINS'],
                               'O_ops... %s failed!' % app.config['PROJECT'],
                               (app.config['MAIL_USERNAME'],
                                app.config['MAIL_PASSWORD']))
    mail_handler.setLevel(ERROR)
    mail_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(mail_handler)


def configure_hook(app):
    """Configure Application-wide Flask request processing cycle hooks."""

    @app.before_request
    def before_request():
        pass


def configure_services(app, testing):
    """
    Configure services and resources which should be
    instantiated and made available in the app context.

    :param app - Flask app instance
    :param testing - (bool) testing mode flag

    """
    if not app.testing:
        pass
       

def configure_error_handlers(app):
    """Generic error-handling logic."""
    # Following snippet adapted from: http://flask.pocoo.org/snippets/83/
    def make_json_error(exc):
        message = exc.description
        error(message)
        response = jsonify(message=message)
        response.status_code = (exc.code
                                if isinstance(exc, HTTPException)
                                else 500)
        return response

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error
