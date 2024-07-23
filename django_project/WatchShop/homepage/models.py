from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Watches(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class WatchesUploads(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="watch_images/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(WatchesUploads)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(WatchesUploads)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)