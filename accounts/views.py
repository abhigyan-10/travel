from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy  # Added for better login redirection
from .models import Review

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        print(f"Login attempt for: {username}")
        
        user = auth.authenticate(username=username, password=password)
        
        print(f"Authentication result: {user}")
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'login.html')
    
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect("/register/")

            elif User.objects.filter(email=email).exists(): 
                messages.info(request,'Email taken')
                return redirect("/register/")

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("user created")
                auth.login(request,user)
                return redirect("/")

        else:
            messages.info(request,'password does not match')
            return redirect('/register/')
        
        # return redirect('/')

    else:
        return render(request,'register.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')

def booking(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        time = request.POST.get("time")

        # Save to database
        new_booking = Booking(name=name, email=email, date=date, time=time)
        new_booking.save()

        messages.success(request, "Your booking has been confirmed!")

        return redirect("booking")  # Redirect to avoid form resubmission

    return render(request, "booking.html")

@login_required(login_url=reverse_lazy('login')) # Pass a query parameter
def submit_review(request):
    if request.method == "POST":
        text = request.POST.get("review_text")
        if text.strip():
            review = Review(user=request.user, text=text)
            review.save()
            messages.success(request, "Review submitted successfully!")
        else:
            messages.error(request, "Review cannot be empty!")
    return redirect("/")  # Redirect to home after submission

@login_required(login_url=reverse_lazy('login'))  # Pass a query parameter
def like_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user in review.likes.all():
        review.likes.remove(request.user)  # Unlike
    else:
        review.likes.add(request.user)  # Like
    return redirect("/")  # Redirect to home page