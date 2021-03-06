from django.test import TestCase

from rest_assured.testcases import CreateAPITestCaseMixin
from tests.app.factories import StuffFactory
from tests.app.models import Stuff
from tests.mocking.test_base import MockTestCase


class TestCreateTestCase(TestCase):
    def get_case(self, **kwargs):
        class MockCreateTestCase(CreateAPITestCaseMixin, MockTestCase):
            base_name = kwargs.pop('base_name', 'stuff')
            factory_class = StuffFactory
            create_data = {"name": "moar stuff"}

        self.case_class = MockCreateTestCase

        return MockCreateTestCase(**kwargs)

    def test_get_create_url(self):
        instance = self.get_case(methodName='dummy')
        assert instance.get_create_url() == '/stuff/'

    def test_get_create_data(self):
        instance = self.get_case(methodName='dummy')
        assert instance.get_create_data() is self.case_class.create_data

    def test_get_create_response(self):
        instance = self.get_case(methodName='dummy')
        assert instance.get_create_response()

    def test_get_lookup_from_response(self):
        instance = self.get_case(methodName='dummy')
        response = instance.get_create_response()
        assert instance.get_lookup_from_response(response.data)

    def test_test_create(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        response, created = instance.test_create()
        assert response
        assert created
        assert isinstance(created, Stuff)
        assert response.data['name'] == created.name

        # try again using a different lookup field
        instance.response_lookup_field = 'name'
        instance.lookup_field = 'name'
        response, created = instance.test_create({'name': 'unique stuff'})
        assert response
        assert created
        assert isinstance(created, Stuff)
        assert response.data['name'] == created.name

    def test_test_create_with_hyperlinkedmodelserializer(self):
        instance = self.get_case(methodName='dummy', base_name='stuff-linked')
        instance.setUp()
        instance.response_lookup_field = 'name'
        instance.lookup_field = 'name'
        response, created = instance.test_create({'name': 'moar unique stuff'})
        assert response
        assert created
        assert isinstance(created, Stuff)
        assert response.data['name'] == created.name
        assert response.data['url']
