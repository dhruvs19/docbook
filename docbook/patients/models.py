from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
import datetime
from django.core.validators import FileExtensionValidator

class Patients(models.Model):
    UserID          = models.ForeignKey(User, on_delete = CASCADE, unique = True, primary_key = True)
    ProfilePicture  = models.ImageField(upload_to = 'patients/profile_pictures/', null = True,default='patients/profile_images/profile-default.png')
    FirstName       = models.CharField(max_length = 65)
    LastName        = models.CharField(max_length = 65)
    Address         = models.CharField(max_length = 200)
    PhoneNumber     = models.CharField(max_length = 200)
    DOB             = models.DateField(null = True)
    BloodGroup      = models.CharField(max_length = 5)

    def __str__(self):
        return self.UserID.username

    @classmethod
    def calculate_age(cls, DOB):
        today = datetime.date.today()
        years = today.year - DOB.year
        if today.month < DOB.month or (today.month == DOB.month and today.day < DOB.day):
            years -= 1
        return years


class Diagnosis(models.Model):
    ReportID            = models.CharField(max_length=20, primary_key= True, default='0')
    PatientUser         = models.ForeignKey(Patients, on_delete = CASCADE, null=True, blank=True)
    DiagnosisName       = models.CharField(max_length = 100, null=True)
    Document            = models.FileField(upload_to = 'patients/medical-history/', null = True, validators=[FileExtensionValidator(allowed_extensions=['pdf','txt','jpg','png','docx','doc'])])

    def __str__(self):
        return self.ReportID 