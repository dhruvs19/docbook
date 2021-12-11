from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render
from doctor.models import *

class HomepageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        context['specializations'] = Specialization.objects.all()
        return context


class AboutPage(TemplateView):
    template_name = "about.html"

class ContactPage(TemplateView):
    template_name = "contact.html"