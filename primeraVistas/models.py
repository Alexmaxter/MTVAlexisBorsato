from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    date_of_birth = models.DateField(null=True)
    city = models.CharField(max_length=60)
