from django.shortcuts import render
from django.http import HttpResponse
from .models import Watches

# Create your views here.

def Home(request):
    watches = Watches.objects.all()
    context = {'watches_t' : watches}
    return render(request, "home.html", context)

def About(request):
    return render(request, "about.html")