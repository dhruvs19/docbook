from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.

class Users(models.Model):
    UserID      = models.IntegerField( primary_key = True)
    UserName    = models.CharField(max_length = 65)
    Email       = models.EmailField()
    Password    = models.CharField(max_length = 65)
    UserType    = models.CharField(max_length = 10)

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5}".format(
            self,self.UserID, self.UserName, self.Email, self.Password, self.UserType)


class Patients(models.Model):
    PatientId   = models.IntegerField(primary_key = True)
    UserID      = models.ForeignKey(Users, on_delete = CASCADE)
    FirstName   = models.CharField(max_length = 65)
    LastName    = models.CharField(max_length = 65)
    Address     = models.CharField(max_length = 200)
    PhoneNumber = models.IntegerField()
    DOB         = models.DateField()
    BloodGroup  = models.CharField(max_length = 5)

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} ".format(
            self, self.PatientId, self.UserID, self.FirstName, self.LastName, self.Address, self.PhoneNumber, self.DOB, self.BloodGroup)