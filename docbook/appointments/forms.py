from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets, DateField
from .models import Appointments
from patients.models import Patients
from doctor.models import DocProfile


class BookAppointmentForm(ModelForm):

    class Meta:
        model = Appointments
        fields = ['AppointmentDate', 'DoctorUser']
        widgets = { 
            'AppointmentDate': widgets.DateInput(attrs = { 'type': 'date' })
        }
        labels = {
            "AppointmentDate": "Appointment Date",
            "DoctorUser": "Select Doctor"
        }
        
    
    def __init__(self, *args, **kwargs):
        super(BookAppointmentForm, self).__init__(*args, **kwargs)
            
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control floating'

            if visible.field.widget.input_type == "select":
                visible.field.widget.attrs['class'] = "form-select form-control floating"
    

