from tkinter import CASCADE
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    fullName = models.CharField(max_length=40)
    floorNo = models.IntegerField()
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    totalVolume = models.IntegerField(default=0)

    def __str__(self):
        return self.fullName

class UserShower(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    volume = models.FloatField()

    def __str__(self):
        return f"{str(self.user)}: {str(self.date)}"