from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout, name='logout'),
    path("booking/",views.booking,name='booking'),
    path("submit_review/", views.submit_review, name="submit_review"),
    path("like_review/<int:review_id>/", views.like_review, name="like_review"),
]

