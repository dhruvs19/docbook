from os import name
from django.urls import path
from django.urls import re_path
from django.conf import settings
from .views  import *
from . import views

app_name = 'patients'

urlpatterns = [
    path('patient-dashboard/', PatientDashboard.as_view(), name = "dashboard"),
    path('profile-settings/', ProfileSettings.as_view(), name = "settings"),
    path('add-diagnosis/', AddToMedicalHistory.as_view(), name = "add-diagnosis"),
    path('medical-records/', ViewMedicalHistory.as_view(), name = "medical-history"),
    re_path(r'^get-report/(?P<ReportID>\w{9})/$', downloadReport.as_view(), name = "downloadReport")
    ]