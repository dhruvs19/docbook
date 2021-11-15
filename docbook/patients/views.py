from django.shortcuts import render
from django.http import HttpResponse
from patients.models import Patients

# Create your views here.
def PatientProfile(request):
    return render(request, 'patients/profile.html')


def testProfile(request):
    return render(request, 'patients/test.html')


def testViewProfile(request):
    profiles = Patients.objects.all()
    stu = {
        "profile_number": profiles
    }
    return render(request, 'patients/testView.html', stu)


def savePatient(request):
    if request.method=="POST":   
        FirstName   = request.POST['FirstName']
        LastName    = request.POST['LastName']
        Address     = request.POST['Address']
        PhoneNumber = request.POST['PhoneNumber']
        DOB         = request.POST['DOB']
        BloodGroup  = request.POST['BloodGroup']

        patient_data = Patients.objects.create(  
        FirstName   = FirstName  ,
        LastName    = LastName  , 
        Address     = Address    ,
        PhoneNumber = PhoneNumber,
        DOB         = DOB   ,     
        BloodGroup  = BloodGroup )

        patient_data.save()
        return render(request, 'patients/test.html')
    else:
        return render(request,'test.html') 