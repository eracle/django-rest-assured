from rest_framework import serializers

from tests.app.models import Stuff, RelatedStuff, ManyRelatedStuff


class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ['id', 'name', 'answer']


class StuffHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stuff
        fields = ['name', 'answer', 'url']


class RelatedStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedStuff
        fields = ['thing']


class RelatedStuffHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RelatedStuff
        fields = ['thing']

    thing = serializers.HyperlinkedRelatedField(queryset=Stuff.objects.all(),
                                                view_name='stuff-linked-detail')


class ManyRelatedStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManyRelatedStuff
        fields = ['stuff']


class ManyRelatedStuffHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ManyRelatedStuff
        fields = ['stuff']

    # stuff = serializers.HyperlinkedRelatedField(queryset=Stuff.objects.all(), many=True)
