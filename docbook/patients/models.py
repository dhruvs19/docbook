from django.db import models
from django.db.models.base import Model
from authuser import *


# Create your models here.
class Patients(models.Model):
    FirstName  = models.CharField(max_length = 65)
    LastName  = models.CharField(max_length = 65)
    Address = models.CharField(max_length = 200)
    PhoneNumber = models.IntegerField()
    DOB = models.DateField()
    BloodGroup = models.CharField(max_length = 5)
    RegistrationNumber = models.ForeignKey()