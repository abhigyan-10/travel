from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):
    return render(request,'home.html', {'name':'bitan'})

def add(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    result = val1 + val2

    return render(request, "result.html" , {'result': result})


