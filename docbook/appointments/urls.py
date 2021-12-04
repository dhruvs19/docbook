from os import name
from django.urls import path
from django.urls import re_path
from django.conf import settings
from .views  import *
from django.conf.urls.static import static

app_name = 'appointments'

urlpatterns = [
    path('book-appointment/', BookAppointment.as_view(), name = "book"),
    path('view-appointment/', ViewAppointment.as_view(), name = "list"),
    re_path(r'^appointment-details/(?P<appointment_id>\w{0,50})/$', AppointmentDetails.as_view(), name = "details"),
    re_path(r'^cancel-appointment/(?P<appointment_id>\w{0,50})/$', CancelAppointment.as_view(), name = "cancel")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)