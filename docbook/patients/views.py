from django.views.generic import View, TemplateView
from django.template.response import TemplateResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from .forms import PatientsForm
from .models import Patients
from appointments.models import Appointments
import datetime


class ProfileSettings(View):
    template_name = "patients/profile-settings.html"

    # get request to ProfileSettings page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            patient_row = Patients.objects.get(UserID = self.request.user)
            context={
                "patient_form":PatientsForm(instance = patient_row),
                "patient_details":patient_row,
                "patient_age": Patients.calculate_age(patient_row.DOB)}
            return(TemplateResponse(self.request, self.template_name, context))
        else:   
            return redirect(reverse("core:home"))

    def post(self, *args, **kwargs):
        patient_row = Patients.objects.get(UserID = self.request.user)
        form = PatientsForm(self.request.POST, self.request.FILES, instance =  patient_row)
        if form.is_valid():
            form.save()
            messages.success(self.request, "Profile Saved!" )
        else:
            messages.error(self.request, "Unsuccessful updation!. Invalid information.")
        patient_row = Patients.objects.get(UserID = self.request.user)
        context={
            "patient_form":PatientsForm(instance = patient_row),
            "patient_details":patient_row,
            "patient_age": Patients.calculate_age(patient_row.DOB)}
        return(TemplateResponse(self.request, self.template_name, context))

class PatientDashboard(View):
    template_name = "patients/patient-dashboard.html"

    # get request to patient-dashboard page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            patient_row = Patients.objects.get(UserID = self.request.user)
            patient_appointments = Appointments.objects.all().filter(PatientUser = patient_row).order_by('-BookingTime')
            context = {
                "patient_details":patient_row,
                "patient_age": Patients.calculate_age(patient_row.DOB),
                "patient_appointments":patient_appointments }
            return(TemplateResponse(self.request, self.template_name, context))
        else:   
            return redirect(reverse("core:home"))