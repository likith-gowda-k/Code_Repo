from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('upload', views.Upload, name = "upload_images"),
    path('login', views.login_page, name = "login"),
    path('signup', views.signup_user, name = "signup"),
    path('logout', views.logout_user, name = "logout"),
]
