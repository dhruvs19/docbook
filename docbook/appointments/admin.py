from django.contrib import admin

from django.contrib import admin
from .models import *

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointments, AppointmentAdmin)