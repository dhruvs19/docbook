from django.db import models
from django.contrib.auth.models import User

class DocProfile(models.Model):
    profile_image = models.ImageField(upload_to='images',blank=True)
    name = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    reg_clinic_address=models.CharField(max_length=200)
    pincode=models.CharField(max_length=10) 
    age=models.CharField(max_length=10)   
    bio = models.CharField(max_length=200)
    qualification = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    

