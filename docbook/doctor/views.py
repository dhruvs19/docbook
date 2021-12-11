
from django.http.response import HttpResponse
from django.views.generic import ListView, UpdateView
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import *
from .models import *
from appointments.models import *
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import base64
import matplotlib.ticker as ticker
from django.db.models import Count
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import Group
from django.views.generic import View
from django.template.response import TemplateResponse

# To render homepage
class HomeView(ListView):
	model = DocProfile
	template_name = 'doctor/doctor-dashboard.html'

	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			grp = Group.objects.get(name=self.request.user.groups.get())
			doc = DocProfile.objects.get(UserID = self.request.user)
			app = Appointments.objects.filter(DoctorUser=self.request.user.id,Status="Pending")
			context = super(HomeView, self).get_context_data(*args, **kwargs)
			context["doc"] = doc
			context["app"] = app
			context["grp"] = str(grp)
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
			grp = Group.objects.get(name=self.request.user.groups.get())
			doc = DocProfile.objects.get(UserID = self.request.user)
			context = super(UpdateDoctorView, self).get_context_data(*args, **kwargs)
			context["doc"] = doc
			context["grp"] = str(grp)
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")
			
	def get_success_url(self):
		return reverse("doctor:doctor-register",kwargs={'pk':self.request.user.id})

# To view doc profile
class ProfileView(CreateView):
	model = DocProfile
	form_class = DocProfileForm
	template_name = 'doctor/view-profile.html'
	
	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			grp = Group.objects.get(name=self.request.user.groups.get())
			id = self.request.user.id
			update = "/doctor/update/"+ str(id)
			user = DocProfile.objects.get(UserID = self.request.user)
			context = super(ProfileView, self).get_context_data(*args, **kwargs)
			context["grp"] = str(grp)
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
	return redirect('/doctor/view-app/')

# To view the accepted appointment patients
class PatientListView(ListView):
	model = DocProfile
	template_name = 'doctor/patient-list.html'

	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			grp = Group.objects.get(name=self.request.user.groups.get())
			user = DocProfile.objects.get(UserID = self.request.user)
			app = Appointments.objects.filter(DoctorUser=self.request.user.id,Status="Accepted")
			context = super(PatientListView, self).get_context_data(*args, **kwargs)
			context["doc"] = user
			context["patients"] = app
			context["grp"] = str(grp)
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")

# To view the rejected appointment of patients	
class PatientRejListView(ListView):
	model = DocProfile
	template_name = 'doctor/patient-list.html'

	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			user = DocProfile.objects.get(UserID = self.request.user)
			grp = Group.objects.get(name=self.request.user.groups.get())
			app = Appointments.objects.filter(DoctorUser=self.request.user.id,Status="Rejected")
			context = super(PatientRejListView, self).get_context_data(*args, **kwargs)
			context["doc"] = user
			context["patients"] = app
			context["grp"] = str(grp)
			return context
		else:
			messages.error(self.request, "Contact with Admin for registration...")

# To view all appointments
class ViewApp(ListView):
	model = DocProfile
	template_name = "doctor/view-appointment.html"
	def get_context_data(self, *args, **kwargs):
		if DocProfile.objects.filter(UserID = self.request.user).exists():
			user = DocProfile.objects.get(UserID = self.request.user)
			grp = Group.objects.get(name=self.request.user.groups.get())
			app = Appointments.objects.filter(DoctorUser=self.request.user.id)
			context = super(ViewApp, self).get_context_data(*args, **kwargs)
			print(type(grp))
			context["doc"] = user
			context["app"] = app
			context["grp"] = str(grp)
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
	data = request.FILES["document"]
	fs = FileSystemStorage()
	file = fs.save(f"patients/appointment-documents/{data.name}",data)
	file_url = fs.url(file)
	Appointments.objects.filter(AppointmentID=appointment_id).update(Remarks=request.POST["remark"],AppointmentFee=request.POST["amount"],Document=file_url)
	return redirect("/doctor/view-app/")

class DoctorPublicProfile(View):
	template_name = "doctor/doctor_public_profile.html"

	def get(self, *args, **kwargs):
		doctor_row = DocProfile.objects.get(UserID = kwargs['UserID'])
		context={
			"doctorGrpah":generateDoctorAppointmentGraph(doctor_row),
			"doctor_details":doctor_row}
		return(TemplateResponse(self.request, self.template_name, context))

class GetDoctorListing(View):
	def get(self, *args, **kwargs):
		filterQuery = {}
		context = {
			'locations': Location.objects.all(),
			'specializations': Specialization.objects.all()
		}

		if 'location' in self.request.GET:
			filterQuery['location'] = self.request.GET['location']
		if 'gender' in self.request.GET:
			filterQuery['gender'] = self.request.GET['gender']
		if 'specs' in self.request.GET:
			filterQuery['specialization'] = self.request.GET['specs']

		context['doctor_list'] = DocProfile.objects.filter(**filterQuery)
		
		return render(self.request, "doctor/doctor-list.html", context)


def generateDoctorAppointmentGraph(docUser):
	res = Appointments.objects.filter(DoctorUser = docUser).values('Status').annotate(scount=Count('Status')).order_by('Status')
	app_count = []
	sts_list = []
	for i,c in enumerate(res):
		app_count.append(c['scount'])
		sts_list.append(c['Status'])

	x = np.array(sts_list)
	y = np.array(app_count)

	plt.locator_params(axis="y", integer=True, tight=True)

	plt.bar(x,y, color = '#272b41', width=.5)
	plt.xlabel("Status")
	plt.ylabel("Appointments")
	plt.title("Appointments vs Status")

	buffer = BytesIO()
	filename = 'media/doctors/graphs/'+ docUser.name +'.png'
	plt.savefig(filename)
	b64 = base64.b64encode(buffer.getvalue()).decode()
	buffer.close()
	return b64