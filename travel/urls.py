from django.urls import path
from .views import create_superuser_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('add-trip/', views.add_trip, name='add_trip'),
    path('create-superuser/', create_superuser_view),
]