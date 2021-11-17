from django.views.generic import View, TemplateView
from django.template.response import TemplateResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from .forms import PatientsForm

# Create your views here
# 
class PatientProfile(View):
    template_name = 'patients/profile.html'
    
    def get(self, *args, **kwargs):
        return redirect(reverse("patients:patient_profile_url"))

class ProfileSettings(View):
    template_name = "patients/profile-settings.html"

    # get request to register page
    def get(self, *args, **kwargs):
        context={
            "body_class":"profile-page",
            "patient_form":PatientsForm()}
        return(TemplateResponse(self.request, self.template_name, context))

    def post(self, *args, **kwargs):
            form = PatientsForm(self.request.POST)
            if form.is_valid():
                patient = form.save()
                messages.success(self.request, "Profile Saved!" )
                return redirect("patients:patient_profile_url")
            context={
                    "body_class":"account-page",
                    "register_form":form}
            messages.error(self.request, "Unsuccessful registration. Invalid information.")
            return(TemplateResponse(self.request, self.template_name, context))
        