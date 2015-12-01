from nose.tools import eq_

from rodeo.extensions import db
from rodeo.models.picture import Picture
from rodeo.tests.base import FlaskTestCase
from rodeo.tests.fixtures import PICTURE


class PaymentMethodTestCase(FlaskTestCase):

    def test_create_and_retrieve_valid_picture(self):
        picture = Picture(**PICTURE)

        db.session.add(picture)
        db.session.commit()

        saved_picture = Picture.query.get(PICTURE["id"])
        eq_(saved_picture, picture)
