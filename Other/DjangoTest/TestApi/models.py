from django.db import models

class Country(models.Model):
    visitDate = models.DateField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class City(models.Model):
    visitDate = models.DateField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

