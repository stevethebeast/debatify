from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer, momSerializer
from .models import Hero, yourMom


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class MomViewSet(viewsets.ModelViewSet):
    queryset = yourMom.objects.all().order_by('name')
    serializer_class = momSerializer