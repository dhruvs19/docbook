from django.shortcuts import render
from django.http import HttpResponse
from docbook import patients

from docbook.patients.form import PatientFormset
from docbook.patients.models import Patients

# Create your views here.
def PatientProfile(request):
    return render(request, 'patients/profile.html')


def savePatient(request):
    form = PatientsForm()
    book_formset = PatientFormset(instance = Patients())

    if request.POST:
        form = PatientsForm(request.POST)
        if form.is_valid():
            patients = form.save()
            book_formset = PatientFormset(request.POST, instance = Patients)
            if book_formset.is_valid():
                book_formset.save()
            return redirect('/index/')

    return render_to_response('addbook.html',{
        'form': form, 'formset': book_formset
    },context_instance=RequestContext(request))  
