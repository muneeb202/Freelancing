# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_cash = models.DecimalField(default=100000, decimal_places=2, max_digits=10)

class Record(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stock = models.CharField(max_length=50)
    quantity = models.IntegerField()
    value = models.DecimalField(decimal_places=2, max_digits=10)