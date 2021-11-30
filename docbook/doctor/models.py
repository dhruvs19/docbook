
from django.db import models
from django.db.models.base import Model
from django.urls import reverse, reverse_lazy
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Specialization(models.Model):
    specialization = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.specialization


class Location(models.Model):
    location = models.CharField(max_length=200, primary_key=True)

    # def __str__(self):
    #     return self.location


class DocProfile(models.Model):
    profile_image = models.ImageField(
        upload_to='doctors/profile_images', blank=True, default='doctors/profile_images/profile-default.png')
    UserID = models.ForeignKey(
        User, unique=True, primary_key=True, on_delete=CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    reg_clinic_address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    bio = models.CharField(max_length=200)
    qualification = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization, on_delete=CASCADE)
    location = models.ForeignKey(Location, on_delete=CASCADE)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.UserID.username

    def get_absolute_url(self):
        return reverse('home')
