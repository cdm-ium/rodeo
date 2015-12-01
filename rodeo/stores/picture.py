"""Picture Store."""
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.exceptions import NotFound

from rodeo.extensions import db
from rodeo.models.picture import Picture


class PictureStore(object):

    @classmethod
    def create(cls, picture):
        db.session.add(picture)
        db.session.commit()
        return picture

    @classmethod
    def retrieve(cls, picture_id):
        return db.session.query(Picture).filter(
            Picture.id == picture_id
        ).one()
