from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Home(request):
    return HttpResponse("Hello Django!")

def About(request):
    return HttpResponse("About Page")
