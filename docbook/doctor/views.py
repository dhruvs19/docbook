from django.views.generic import View, TemplateView
from django.template.response import TemplateResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from .forms import DocProfileForm
from .models import DocProfile


class Profile_submit(View):
    template_name = "doctor/step1.html"

    def get(self, *args, **kwargs):

        if self.request.user.is_authenticated:

            doctor_row = DocProfile.objects.get(UserID=self.request.user)
            context = {
                "body_class": "profile-page",
                "doctor_form": DocProfileForm(instance=doctor_row)}
            return(TemplateResponse(self.request, self.template_name, context))
        else:
            return redirect(reverse("core:home"))

    def post(self, *args, **kwargs):
        doctor_row = DocProfile.objects.get(UserID=self.request.user)
        form = DocProfileForm(self.request.POST, instance=doctor_row)
        if form.is_valid():
            form.save()
            img_object = form.instance
            messages.success(self.request, "Profile Saved!")
        else:
            messages.error(
                self.request, "Unsuccessful updation!. Invalid information.")
        context = {
            "body_class": "profile-settings",
            "doctor_form": form,
            "img_object": img_object,
        }
        return(TemplateResponse(self.request, self.template_name, context))
