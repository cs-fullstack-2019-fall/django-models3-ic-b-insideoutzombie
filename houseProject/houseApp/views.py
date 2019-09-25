from django.shortcuts import render
from django.http import HttpResponse
from .models import House

# Create your views here.
def index(request):
    return HttpResponse("Hello Book World")

def addHouse(request):
    house1 = House(address="1546 Washington Ave", bedrooms=4, bathrooms=2, squareFeet=1500)
    house1.save()
    return HttpResponse("House Added Mane")

def allHouse(request):
    houseList = House.objects.all()
    for eachElement in houseList:
        print(eachElement.address)
    return HttpResponse(eachElement.address)
