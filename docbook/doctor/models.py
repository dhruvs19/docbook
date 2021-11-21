
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class DocProfile(models.Model):
    profile_image = models.ImageField(upload_to='images/', blank=True)
    UserID = models.ForeignKey(User, unique=True, primary_key=True, on_delete=CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    reg_clinic_address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    bio = models.CharField(max_length=200)
    qualification = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.UserID.username