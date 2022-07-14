from django.shortcuts import render

from rest_framework import viewsets

from TestApi.serializers import CountrySerializer, CitySerializer
from TestApi.models import Country, City

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
