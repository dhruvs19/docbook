from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
import datetime
from djongo import models

class Diagnosis(models.Model):
    DiagnosisID         = models.IntegerField(primary_key = True)
    DiagnosisType       = models.CharField(max_length = 65)
    DiagnosisDetails    = models.TextField()
    Document            = models.FileField(upload_to = 'patients/profile_pictures/', null = True)      


class Patients(models.Model):
    UserID          = models.ForeignKey(User, on_delete = CASCADE, unique = True, primary_key = True)
    ProfilePicture  = models.ImageField(upload_to = 'patients/profile_pictures/', null = True)
    FirstName       = models.CharField(max_length = 65)
    LastName        = models.CharField(max_length = 65)
    Address         = models.CharField(max_length = 200)
    PhoneNumber     = models.CharField(max_length = 200)
    DOB             = models.DateField(null = True)
    BloodGroup      = models.CharField(max_length = 5)
    MedicalRecords  = models.EmbeddedField(model_container = Diagnosis, null=True)

    def __str__(self):
        return self.UserID.username

    @classmethod
    def calculate_age(cls, DOB):
        today = datetime.date.today()
        years = today.year - DOB.year
        if today.month < DOB.month or (today.month == DOB.month and today.day < DOB.day):
            years -= 1
        return years