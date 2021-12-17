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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
def create_unique_id():
    return ''.join(random.choices(string.digits, k=9))


def create_appointment_id():
    id = create_unique_id()
    while Appointments.objects.filter(AppointmentID=id).exists():
        id = create_unique_id()
    return id


class BookAppointment(LoginRequiredMixin, View):
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
            return redirect(reverse("appointments:list"))
        else:   
            return redirect(reverse("core:home"))

class ViewAppointment(View):
    template_name = "appointments/view-appointment.html" 
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            patient_row = Patients.objects.get(UserID = self.request.user)
            patient_appointments = Appointments.objects.all().filter(PatientUser = patient_row).order_by('-BookingTime')
            context={
                "patient_name":patient_row.UserID,
                "patient_image":patient_row.ProfilePicture,
                "patient_dob":patient_row.DOB,
                "patient_appointments":patient_appointments, 
                "patient_age": Patients.calculate_age(patient_row.DOB)}
            return(TemplateResponse(self.request, self.template_name, context))
        else:   
            return redirect(reverse("core:home"))

class AppointmentDetails(View):
    template_name = "appointments/appointment-details.html"
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            patient_row = Patients.objects.get(UserID = self.request.user)
            appointment_details = Appointments.objects.get(AppointmentID = kwargs['appointment_id'])
            doctor_row = DocProfile.objects.get(UserID = appointment_details.DoctorUser)
            context={
                "clinic_address":doctor_row.reg_clinic_address,
                "patient_name":patient_row.UserID,
                "patient_image":patient_row.ProfilePicture,
                "patient_dob":patient_row.DOB,
                "appointment_details":appointment_details, 
                "patient_age": Patients.calculate_age(patient_row.DOB)}
            return(TemplateResponse(self.request, self.template_name, context))
        else:   
            return redirect(reverse("core:home"))

class CancelAppointment(View):

    # get request to book-appointment page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            # patient_row = Patients.objects.get(UserID = self.request.user)
            Appointments.objects.filter(AppointmentID = kwargs['appointment_id']).update(Status = 'Cancelled')
            messages.success(self.request, "Appointment Cancelled!" )
            return redirect(reverse("appointments:list"))
        else:   
            return redirect(reverse("core:home"))