from rest_framework import viewsets

from tests.app.models import Stuff, RelatedStuff, ManyRelatedStuff
from tests.app.serializers import StuffSerializer, StuffHyperlinkedSerializer, RelatedStuffSerializer, \
    RelatedStuffHyperlinkedSerializer, ManyRelatedStuffSerializer, ManyRelatedStuffHyperlinkedSerializer


class StuffViewSet(viewsets.ModelViewSet):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
    paginate_by = 10


class StuffHyperlinkedViewSet(viewsets.ModelViewSet):
    queryset = Stuff.objects.all()
    serializer_class = StuffHyperlinkedSerializer
    paginate_by = 10


class RelatedStuffViewSet(viewsets.ModelViewSet):
    queryset = RelatedStuff.objects.all()
    serializer_class = RelatedStuffSerializer
    paginate_by = 10


class RelatedStuffHyperlinkedViewSet(viewsets.ModelViewSet):
    queryset = RelatedStuff.objects.all()
    serializer_class = RelatedStuffHyperlinkedSerializer
    paginate_by = 10


class ManyRelatedStuffViewSet(viewsets.ModelViewSet):
    queryset = ManyRelatedStuff.objects.all()
    serializer_class = ManyRelatedStuffSerializer
    paginate_by = 10


class ManyRelatedStuffHyperlinkedViewSet(viewsets.ModelViewSet):
    queryset = ManyRelatedStuff.objects.all()
    serializer_class = ManyRelatedStuffHyperlinkedSerializer
    paginate_by = 10
