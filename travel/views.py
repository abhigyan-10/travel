from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination, Popular, Trip
from django.contrib.auth.decorators import login_required
from accounts.models import Review 
from .forms import TripForm
from django.http import HttpResponse
from .create_superuser import create_admin

# Create your views here.

def index(request):
    dests = Destination.objects.all()
    pops = Popular.objects.all()
    reviews = Review.objects.order_by("-created_at")[:5] 
    trips = Trip.objects.all().order_by('-date')  # Latest trips first
    return render(request, "index.html",{'dests': dests, 'pops':pops, 'reviews': reviews, 'trips': trips})

def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after submission
    else:
        form = TripForm()
    return render(request, 'add_trip.html', {'form': form})


def create_superuser_view(request):
    message = create_admin()
    return HttpResponse(message)

def about(request):
    reviews = Review.objects.order_by("-created_at")[:5] 
    trips = Trip.objects.all().order_by('-date')  # Latest trips first
    return render(request, 'travel/about.html',{'reviews': reviews, 'trips': trips})