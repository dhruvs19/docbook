from os import name
from django.urls import path
from django.conf import settings
from .views  import *

app_name = 'patients'

urlpatterns = [
    path('patient-dashboard/', PatientDashboard.as_view(), name = "patient_dashboard_url"),
    path('profile-settings/', ProfileSettings.as_view(), name = "profile_settings_url")
]