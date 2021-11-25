from django.views.generic import View, TemplateView
from django.template.response import TemplateResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from .forms import PatientsForm
from .models import Patients

# Create your views here
# 
class PatientProfileList(View):
    template_name = 'patients/profilelist.html'
    
    def get(self, *args, **kwargs):
         return(TemplateResponse(self.request, self.template_name))

class ProfileSettings(View):
    template_name = "patients/profile-settings.html"

    # get request to ProfileSettings page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            patient_row = Patients.objects.get(UserID = self.request.user)
            context={
                "body_class":"profile-page",
                "patient_form":PatientsForm(instance = patient_row)}
            return(TemplateResponse(self.request, self.template_name, context))
        else:   
            return redirect(reverse("core:home"))

    def post(self, *args, **kwargs):
        patient_row = Patients.objects.get(UserID = self.request.user)
        form = PatientsForm(self.request.POST, instance =  patient_row)
        if form.is_valid():
            form.save()
            messages.success(self.request, "Profile Saved!" )
        else:
            messages.error(self.request, "Unsuccessful updation!. Invalid information.")
        context={
            "body_class":"profile-settings",
            "patient_form":form}
        return(TemplateResponse(self.request, self.template_name, context))
        