
from django.urls import path
from . import views

urlpatterns = [
    path('',views.DocRegisterView,name="doctor-register"),
    path('doctor-register-step1/',views.DocRegisterView1,name="doctor-register-step1"),
    path('doctor-register-step1/profile_submit',views.profile_submit,name="profile_submit")
]
