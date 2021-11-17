from os import name
from django.urls import path
from django.conf import settings
from .views  import *

app_name = 'patients'

urlpatterns = [
    path('profile/', PatientProfile.as_view(), name = "patient_profile_url"),
    path('profile-settings/', ProfileSettings.as_view(), name = "profile_settings_url")
]