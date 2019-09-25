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

def printBed(request):
    allHome = House.objects.all()
    for eachElement in allHome:
        if(allHome.bedrooms > 2):
            print(eachElement)
        return HttpResponse("Bedrooms Checked")

def squareFeet(request):
    allhome = House.objects.all()
    for eachElement in allHome:
        if(eachElement.bathrooms > 5):
            eachElement.squareFeet = 9999
            print(eachElement.squareFeet)
        else:
            
