from django.test import TestCase

from rest_assured.testcases import ListAPITestCaseMixin
from tests.app.factories import StuffFactory
from tests.mocking.test_base import MockTestCase


class TestListTestCase(TestCase):
    def get_case(self, **kwargs):
        class MockListTestCase(ListAPITestCaseMixin, MockTestCase):
            base_name = 'stuff'
            factory_class = StuffFactory

        self.case_class = MockListTestCase

        return MockListTestCase(**kwargs)

    def test_get_list_url(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        assert instance.get_list_url() == '/stuff/'

    def test_get_list_response(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        response = instance.get_list_response()
        assert response
        assert response.status_code == 200
        assert response.data

    def test_test_list(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        response = instance.test_list()
        assert response
