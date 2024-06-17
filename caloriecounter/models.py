from django.db import models
from django.utils import timezone


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    #date = models.DateTimeField(auto_now_add=True)
