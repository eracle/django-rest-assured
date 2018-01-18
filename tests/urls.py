from rest_framework import routers

from tests.app.views import StuffViewSet, StuffHyperlinkedViewSet, RelatedStuffViewSet, RelatedStuffHyperlinkedViewSet

router = routers.DefaultRouter()

router.register(r'stuff', StuffViewSet,
                base_name='stuff')

router.register(r'stuff-linked', StuffHyperlinkedViewSet,
                base_name='stuff-linked')

router.register(r'related-stuff', RelatedStuffViewSet,
                base_name='relatedstuff')

router.register(r'related-stuff-linked', RelatedStuffHyperlinkedViewSet,
                base_name='relatedstuff-linked')

router.register(r'many-related-stuff', RelatedStuffViewSet,
                base_name='manyrelatedstuff')

router.register(r'many-related-stuff-linked', RelatedStuffHyperlinkedViewSet,
                base_name='manyrelatedstuff-linked')

urlpatterns = router.urls
