from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who wrote the review
    text = models.TextField()  # Review text
    likes = models.ManyToManyField(User, related_name="liked_reviews", blank=True)  # Users who liked the review
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def total_likes(self):
        return self.likes.count()  # Returns total number of likes
