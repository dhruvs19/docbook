from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
import os
from uuid import uuid4
# Create your models here.

class Patients(models.Model):
    UserID          = models.ForeignKey(User, on_delete = CASCADE, unique = True, primary_key = True)
    ProfilePicture = models.ImageField(upload_to = 'patients/profile_pictures/')
    FirstName       = models.CharField(max_length = 65)
    LastName        = models.CharField(max_length = 65)
    Address         = models.CharField(max_length = 200)
    PhoneNumber     = models.CharField(max_length = 200)
    DOB             = models.DateField(null = True)
    BloodGroup      = models.CharField(max_length = 5)

    def __str__(self):
        return self.UserID.username