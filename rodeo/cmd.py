"""
Console (CLI) entry points.

"""
from rodeo.app import create_app
from rodeo.extensions import db

from rodeo.models.picture import Picture  # noqa

def createall():
    """
    Initialize Database and populate with seed data.

    """
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        db.session.commit()
