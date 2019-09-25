from django.db import models
from django.utils import timezone

# Create your models here.
class House(models.Model):
    address = models.CharField(max_length = 200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    squareFeet = models.IntegerField()
