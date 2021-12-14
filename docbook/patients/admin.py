from django.contrib import admin
from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'FirstName', 'LastName', 'DOB')
admin.site.register(Patients, PatientAdmin)