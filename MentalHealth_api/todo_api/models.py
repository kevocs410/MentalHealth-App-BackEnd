from django.db import models

# Create your models here.

class Todo(models.Model):
    rating=models.IntegerField()
    workout=models.CharField(max_length=32)
    time=models.CharField(max_length=32)