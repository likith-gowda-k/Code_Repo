
from django.urls import path
from django.http import HttpResponse
from . import views





urlpatterns = [
    path('',views.Home, name="home"),
    path('about/',views.About,name="about")
]
