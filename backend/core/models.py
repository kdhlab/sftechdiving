from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    depth = models.IntegerField()
    gas_mix = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    max_divers = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.trip.title}"
