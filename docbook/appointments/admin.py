from django.contrib import admin

from django.contrib import admin
from .models import *

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('AppointmentID', 'DoctorUser', 'PatientUser','AppointmentFee','BookingTime' )
admin.site.register(Appointments, AppointmentAdmin)