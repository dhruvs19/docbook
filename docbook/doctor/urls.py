from os import name
from django.urls import path
from django.conf import settings
from .views  import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'doctor'

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('accept/<int:pk>', views.acceptView, name = "accept-view"),
    path('patient-list/', PatientListView.as_view(), name = "accept-view"),
    path('rej-patient-list/', PatientRejListView.as_view(), name = "reject-view"),
    path('profile/', ProfileView.as_view(), name = "profile-view"),
    path('update/<int:pk>', UpdateDoctorView.as_view(),name = "doctor-register"),
    path('delete/<int:pk>', views.deleteView, name = "delete-view"),
    path('doctor_list', GetDoctorListing.as_view(), name = "doctor-list"),
]
