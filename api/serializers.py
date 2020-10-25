from rest_framework import serializers

from .models import Hero, yourMom

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class momSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = yourMom
        fields = ('name', 'alias')