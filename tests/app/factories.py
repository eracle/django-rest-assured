import factory
from django.contrib.auth import get_user_model

from rest_assured.testcases import BaseRESTAPITestCase
from tests.app.models import Stuff, RelatedStuff, ManyRelatedStuff

User = get_user_model()


class StuffFactory(factory.DjangoModelFactory):
    name = 'name of stuff'
    answer = 42

    class Meta:
        model = Stuff


class RelatedStuffFactory(factory.DjangoModelFactory):
    class Meta:
        model = RelatedStuff


class ManyRelatedStuffFactory(factory.DjangoModelFactory):
    thing1 = factory.RelatedFactory(StuffFactory, factory_related_name='manyrelatedstuff_set',
                                    name='referenced stuff 1')
    thing2 = factory.RelatedFactory(StuffFactory, factory_related_name='manyrelatedstuff_set',
                                    name='referenced stuff 2')

    class Meta:
        model = ManyRelatedStuff


class UserFactory(factory.DjangoModelFactory):
    username = 'username'

    class Meta:
        model = User


class StuffTestCase(BaseRESTAPITestCase):
    factory_class = StuffFactory
    user_factory = UserFactory

    def __init__(self, *args, **kwargs):
        self._pre_setup()
        super().__init__(*args, **kwargs)

    def _pre_setup(self):
        self.client = self.client_class()

    def dummy(self):
        pass
