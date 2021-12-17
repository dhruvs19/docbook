import os
import datetime
import random, string
from .models import Patients
from .models import Diagnosis
from django.conf import settings
from django.contrib import messages
from appointments.models import Appointments
from django.http import HttpResponse, Http404
from .forms import DiagnosisForm, PatientsForm
from django.views.generic import View, TemplateView
from django.template.response import TemplateResponse
from django.shortcuts import redirect, render, reverse



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

class AddToMedicalHistory(View):
    template_name = "patients/add-diagnosis.html"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            patient_row = Patients.objects.get(UserID = self.request.user)
            context = {
                "diagnosis_form":DiagnosisForm(),
                "patient_details":patient_row,
                "patient_age": Patients.calculate_age(patient_row.DOB)
            }
            return(TemplateResponse(self.request, self.template_name, context))
        else:   
            return redirect(reverse("core:home"))
    
    def post(self, *args, **kwargs):
        form = DiagnosisForm(self.request.POST, self.request.FILES) 
        print(form)
        if form.is_valid():
            diagnosis_obj = form.save(commit=False)
            diagnosis_obj.ReportID = create_diagnosis_id()
            diagnosis_obj.PatientUser = Patients.objects.get(UserID = self.request.user)
            diagnosis_obj.save()
            messages.success(self.request, "Diagnosis Saved!" )
        else:
            messages.error(self.request, "Unsuccessful updation!. Invalid information.")
        return redirect(reverse("patients:dashboard"))

class ViewMedicalHistory(View):
    template_name = "patients/diagnosis-details.html" 
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            patient_row = Patients.objects.get(UserID = self.request.user)
            diagnosis_list = Diagnosis.objects.all().filter(PatientUser = patient_row)
            context={
                "patient_details":patient_row,
                "diagnosis_list":diagnosis_list, 
                "patient_age": Patients.calculate_age(patient_row.DOB)}
            return(TemplateResponse(self.request, self.template_name, context))
        else:   
            return redirect(reverse("core:home"))

class downloadReport(View):

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            Diagnosis_obj = Diagnosis.objects.get(ReportID = kwargs['ReportID'])
            print(Diagnosis_obj.Document)
            file_path = os.path.join(settings.MEDIA_ROOT, str(Diagnosis_obj.Document))
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/*")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                    return response
            raise Http404
        else:   
            return redirect(reverse("core:home"))

def create_unique_id():
    return ''.join(random.choices(string.digits, k=9))

def create_diagnosis_id():
    id = create_unique_id()
    while Diagnosis.objects.filter(ReportID=id).exists():
        id = create_unique_id()
    return id