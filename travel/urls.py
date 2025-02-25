from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-trip/', views.add_trip, name='add_trip'),
    
]