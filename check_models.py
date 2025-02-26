import os
import django

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")  
django.setup()

from travel.models import Destination, Popular, Trip  

# Check if models exist in the database
print(Destination.objects.all())  
print(Popular.objects.all())  
print(Trip.objects.all())  
