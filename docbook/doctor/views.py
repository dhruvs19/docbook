from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView, UpdateView
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import *
from .models import *
from appointments.models import *

# To render homepage
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

# To update the doc profile    
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

# To view doc profile
class ProfileView(CreateView):
	model = DocProfile
	form_class = DocProfileForm
	template_name = 'doctor/view-profile.html'
	
	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			id = self.request.user.id
			update = "/doctor/update/"+ str(id)
			user = DocProfile.objects.get(UserID = self.request.user)
			context = super(ProfileView, self).get_context_data(*args, **kwargs)
			context["doc"] = user
			context["update"] = update
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")

# To accept the appointment
def acceptView(request,pk):
	Appointments.objects.filter(AppointmentID=pk,Status="Pending").update(Status="Accepted")
	return redirect('/doctor/patient-list/')
	

# To reject the appointment
def deleteView(request,pk):
	Appointments.objects.filter(AppointmentID=pk).update(Status="Rejected")
	return redirect('/doctor/')

# To view the accepted appointment patients
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

# To view the rejected appointment patients	
class PatientRejListView(ListView):
	model = DocProfile
	template_name = 'doctor/patient-list.html'

	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			user = DocProfile.objects.get(UserID = self.request.user)
			app = Appointments.objects.filter(DoctorUser=self.request.user.id,Status="Rejected")
			context = super(PatientRejListView, self).get_context_data(*args, **kwargs)
			context["doc"] = user
			context["patients"] = app
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")

# class CancelledAppListView(ListView):
# 	model = DocProfile
# 	template_name = 'doctor/patient-list.html'

# 	def get_context_data(self, *args, **kwargs):
# 		if DocProfile.objects.filter(UserID = self.request.user).exists():
# 			user = DocProfile.objects.get(UserID = self.request.user)
# 			app = Appointments.objects.filter(DoctorUser=self.request.user.id,Status="Cancelled")
# 			context = super(CancelledAppListView, self).get_context_data(*args, **kwargs)
# 			context["doc"] = user
# 			context["patients"] = app
# 			return context
# 		else:
# 			messages.error(self.request, "Contact with Admin for registration...")

# To view all appointments
class ViewApp(ListView):
	model = DocProfile
	template_name = "doctor/view-appointment.html"
	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			user = DocProfile.objects.get(UserID = self.request.user)
			app = Appointments.objects.filter(DoctorUser=self.request.user.id)
			context = super(ViewApp, self).get_context_data(*args, **kwargs)
			context["doc"] = user
			context["app"] = app
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")

# To render the appointment deatails
def appDetails(request,appointment_id):
	ap = Appointments.objects.filter(AppointmentID=appointment_id)
	doc = DocProfile.objects.get(UserID = request.user)
	context = {
		'ap' : ap,
		'doc' : doc,
	}
	return render(request,"doctor/appointment-details.html",context)

# To update the appointment
def updateAppointment(request):
	appointment_id=request.POST["id"]
	print(request.FILES["document"])
	Appointments.objects.filter(AppointmentID=appointment_id).update(Remarks=request.POST["remark"],AppointmentFee=request.POST["amount"],Document=request.FILES["document"])
	return redirect("/doctor/view-app/")