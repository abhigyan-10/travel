from django.contrib import admin
from .models import Destination, Popular
# Register your models here.


# Customize the Destination model in the admin interface
class DestinationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'price', 'days', 'offer')
    
    # Add search functionality
    search_fields = ('name', 'desc')
    
    # Add filters for the list view
    list_filter = ('offer', 'days')
    
    # Make fields editable directly in the list view
    list_editable = ('price', 'offer')

# Customize the Popular model in the admin interface
class PopularAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'plc')
    
    # Add search functionality
    search_fields = ('name',)
    
    # Add filters for the list view
    list_filter = ('plc',)
    
admin.site.register(Destination)
admin.site.register(Popular)