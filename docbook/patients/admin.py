from django.contrib import admin
from .models import *

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patients, PatientAdmin)