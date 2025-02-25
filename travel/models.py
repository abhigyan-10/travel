from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length = 100) # type: ignore
    img = models.ImageField(upload_to='img')
    desc = models.TextField() # type: ignore
    price = models.IntegerField()
    offer = models.BooleanField(default= False) # type: ignore
    days = models.IntegerField()

class Popular(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to= 'img')
    plc = models.IntegerField()


class Trip(models.Model):
    first_name = models.CharField(max_length=100)
    place_name = models.CharField(max_length=200)
    date = models.DateField()
    photo = models.ImageField(upload_to='trip_photos/')
    description = models.TextField()

    def __str__(self):
        return f"{self.first_name} - {self.place_name}"