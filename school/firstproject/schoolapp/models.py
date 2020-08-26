from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=20)
    roll=models.FloatField()
    standard=models.CharField(max_length=20)
    father=models.CharField(max_length=20)
