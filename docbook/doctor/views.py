
from django.http.response import HttpResponse
from django.views.generic import ListView, UpdateView
from django.shortcuts import redirect, render, reverse
#from django.contrib.auth.models import Group
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import *
from .models import DocProfile
from appointments.models import *


class HomeView(ListView):
	model = DocProfile
	template_name = 'doctor/doctor-dashboard.html'

	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			doc = DocProfile.objects.get(UserID = self.request.user)
			app = Appointments.objects.filter(DoctorUser=self.request.user.id,Status="Pending")
			context = super(HomeView, self).get_context_data(*args, **kwargs)
			context["doc"] = doc
			context["app"] = app
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")
    
class UpdateDoctorView(UpdateView):
	model = DocProfile
	form_class = DocProfileForm
	template_name = 'doctor/profile-setting.html'

	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			doc = DocProfile.objects.get(UserID = self.request.user)
			context = super(UpdateDoctorView, self).get_context_data(*args, **kwargs)
			context["doc"] = doc
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")

class ProfileView(CreateView):
	model = DocProfile
	form_class = DocProfileForm
	template_name = 'doctor/view-profile.html'
	
	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			id = self.request.user.id
			update = "/doctor/update/"+str(id)
			user = DocProfile.objects.get(UserID = self.request.user)
			context = super(ProfileView, self).get_context_data(*args, **kwargs)
			context["doc"] = user
			context["update"] = update
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")

def acceptView(request,pk):
	Appointments.objects.filter(AppointmentID=pk,Status="Pending").update(Status="Accepted")
	return redirect('/doctor/')

def deleteView(request,pk):
	Appointments.objects.filter(AppointmentID=pk,Status="Pending").update(Status="Cancelled")
	return redirect('/doctor/')

class PatientListView(ListView):
	model = DocProfile
	template_name = 'doctor/patient-list.html'

	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			user = DocProfile.objects.get(UserID = self.request.user)
			app = Appointments.objects.filter(DoctorUser=self.request.user.id,Status="Accepted")
			context = super(PatientListView, self).get_context_data(*args, **kwargs)
			context["doc"] = user
			context["patients"] = app
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")
	

