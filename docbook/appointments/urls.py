from os import name
from django.urls import path
from django.urls import re_path
from django.conf import settings
from .views  import *

app_name = 'appointments'

urlpatterns = [
    path('book-appointment/', BookAppointment.as_view(), name = "book_appointment_url"),
    path('view-appointment/', ViewAppointment.as_view(), name = "view_appointment_url"),
    re_path(r'^appointment-details/(?P<appointment_id>\w{0,50})/$', AppointmentDetails.as_view(), name = "appointment_details_url")
]