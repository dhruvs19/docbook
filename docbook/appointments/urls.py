from os import name
from django.urls import path
from django.conf import settings
from .views  import *

app_name = 'appointments'

urlpatterns = [
    path('book-appointment/', BookAppointment.as_view(), name = "book_appointment_url")
]