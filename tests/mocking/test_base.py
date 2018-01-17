from django.test import TestCase

from rest_assured.testcases import BaseRESTAPITestCase
from tests.app.factories import UserFactory
from tests.mocking.mocks import MockFactory, MockObject


class MockTestCase(BaseRESTAPITestCase):
    factory_class = MockFactory
    user_factory = UserFactory

    def __init__(self, *args, **kwargs):
        self._pre_setup()
        super(MockTestCase, self).__init__(*args, **kwargs)

    def _pre_setup(self):
        self.client = self.client_class()

    def dummy(self):
        pass


class TestBaseTestCase(TestCase):
    def test_get_factory_class(self):
        instance = MockTestCase(methodName='dummy')
        assert instance.get_factory_class() is MockFactory

    def test_get_object(self):
        instance = MockTestCase(methodName='dummy')
        assert isinstance(instance.get_object(instance.get_factory_class()), MockObject)

    def test_user_exists_and_forced_auth(self):
        instance = MockTestCase(methodName='dummy')
        instance.setUp()
        assert instance.client.handler._force_user is instance.user
