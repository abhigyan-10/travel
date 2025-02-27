from django.db import models
from cloudinary.models import CloudinaryField
# from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length = 100) # type: ignore
    img = CloudinaryField('image')
    desc = models.TextField() # type: ignore
    price = models.IntegerField()
    offer = models.BooleanField(default= False) # type: ignore
    days = models.IntegerField()
    def __str__(self):
        return self.name

class Popular(models.Model):
    name = models.CharField(max_length=50)
    img = CloudinaryField('image')
    plc = models.IntegerField()
    def __str__(self):
        return self.name


class Trip(models.Model):
    first_name = models.CharField(max_length=100)
    place_name = models.CharField(max_length=200)
    date = models.DateField()
    photo = CloudinaryField('image')
    description = models.TextField()

    def __str__(self):
        return f"{self.first_name} - {self.place_name}"