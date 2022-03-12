from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    shop = models.CharField(max_length=30)
    phone = models.IntegerField()
    location = models.CharField(max_length=50)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    shop = models.CharField(max_length=30)
    phone = models.IntegerField()
    location = models.CharField(max_length=50)
    message =  models.TextField()

# Create your models here.
