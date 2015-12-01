"""An ORM model for a Picture."""
from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy_utils import JSONType, UUIDType, ScalarListType

from rodeo.extensions import db

class Picture(db.Model):
    """
    Represents metadata relating to a picture stored someplace with a reference 'file_id'.
    """
    __tablename__ = 'picture'

    created_at = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    author = db.Column(db.String(255))
    file_id = db.Column(db.String(255))
    id = db.Column(UUIDType(), primary_key=True, default=uuid4)
    edition = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super(Picture, self).__init__(**kwargs)
