from django.contrib import admin
from .models import Destination, Popular, Trip
# Register your models here.

admin.site.register(Destination)
admin.site.register(Popular)
admin.site.register(Trip)