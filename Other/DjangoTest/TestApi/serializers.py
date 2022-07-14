from rest_framework import serializers

from TestApi.models import Country, City

#The person of serializer is converting data to JSON
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('visitDate', 'name', 'description')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('visitDate', 'name', 'description', 'country')