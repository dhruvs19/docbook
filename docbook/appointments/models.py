from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from patients.models import Patients
from doctor.models import DocProfile

class Appointments(models.Model):
    AppointmentID       = models.CharField(max_length=20)
    PatientUser         = models.ForeignKey(Patients, on_delete = CASCADE, null=True, blank=True)
    DoctorUser          = models.ForeignKey(DocProfile, on_delete = CASCADE, null=True)
    AppointmentDate     = models.DateField(null = False)
    TimeSlot            = models.CharField(max_length= 20, default="09:00 PM - 10:00 PM")
    AppointmentFee      = models.FloatField(blank=True, default = 0)
    Remarks             = models.CharField(max_length = 200, blank=True, null=True)
    Status              = models.CharField(max_length=50, default = "Pending")
    Document            = models.FileField(upload_to = 'patients/appointment-documents/', null=True, blank=True)
    BookingTime         = models.DateTimeField(null = False, auto_now_add=True)

    def __str__(self):
        return self.AppointmentID
    