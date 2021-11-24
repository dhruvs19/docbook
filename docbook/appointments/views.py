from django.views.generic import View, TemplateView
from django.template.response import TemplateResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.models import User
import random, string
from .models import Appointments
from doctor.models import DocProfile 
from .forms import BookAppointmentForm
import datetime
from patients.models import Patients
 

class BookAppointment(View):
    template_name = "appointments/book-appointment.html"

    # get request to book-appointment page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            patient_row = Patients.objects.get(UserID = self.request.user)
            context={
                "patient_name":patient_row.UserID,
                "patient_image":patient_row.ProfilePicture,
                "patient_dob":patient_row.DOB,
                "BookAppointmentForm":BookAppointmentForm(), 
                "patient_age": Patients.calculate_age(patient_row.DOB)}
            return(TemplateResponse(self.request, self.template_name, context))
        else:   
            return redirect(reverse("core:home"))

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            form = BookAppointmentForm(self.request.POST)

            if form.is_valid():
                appointment_obj = form.save(commit=False)
                appointment_obj.PatientUser = Patients.objects.get(UserID = self.request.user)
                appointment_obj.AppointmentID = create_appointment_id()
                appointment_obj.save()
                messages.success(self.request, "Appointment Booked!" )
            else:
                messages.error(self.request, "Something went wrong!")
            context={"BookAppointmentForm":form}
            return(TemplateResponse(self.request, self.template_name, context))
        else:   
            return redirect(reverse("core:home"))


def create_unique_id():
    return ''.join(random.choices(string.digits, k=9))


def create_appointment_id():
    id = create_unique_id()
    while Appointments.objects.filter(AppointmentID=id).exists():
        id = create_unique_id()
    return id