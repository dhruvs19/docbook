from os import name
from django.urls import path
from .  import views
from django.conf import settings

app_name = 'patients'

urlpatterns = [
    path('profile/', views.PatientProfile)
]