from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def PatientProfile(request):
    return render(request, 'patients/profile.html')


def PatientRegister(request):
    return render(request, 'patients/register.html')