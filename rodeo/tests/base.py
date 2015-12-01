"""Base classes and shared functionality for unit-tests."""
import unittest

from nose.tools import eq_, ok_

from rodeo.app import create_app
from rodeo.extensions import db
# XXX - Model imports here are for SQLAlchemy to automatically initialize tables for unit-tests
from rodeo.models.picture import Picture  # noqa


class FlaskTestCase(unittest.TestCase):
    """
    Base class for Flask tests. Sets up a Flask app in test mode,
    sets up an app_context for the duration of test case, and creates/drops
    the database.

    """
    def setUp(self):
        self.app = create_app(testing=True)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.app_context.pop()

    def assert_valid_response(self, response, data_regexp=None, status_code=None):
        if data_regexp is not None:
            ok_(data_regexp.match(response.data))
        if status_code is not None:
            eq_(response.status_code, status_code,
                "{} != {}. Response data: {}".format(response.status_code,
                                                     status_code, response.data))

    def assert_valid_list_response(self, response, offset, limit, total_num_results):
        """
        Assert response data conforms to our PaginatedList Resource structure.

        :param rseponse - the parsed JSON response payload
        :param offset {int} - expected offset
        :param limit {int} - expected limit
        :param total_num_results {int} - expected total results count

        """
        eq_(response['offset'], offset)
        eq_(response['limit'], limit)
        eq_(response['totalNumResults'], total_num_results)
        eq_(len(response['instances']), min(limit, total_num_results-offset))
