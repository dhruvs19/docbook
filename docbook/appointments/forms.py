from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets, DateField
from .models import Appointments
from patients.models import Patients
from doctor.models import DocProfile


class BookAppointmentForm(ModelForm):
    slots = (
        ('','Select Time Slot'),
        ('08:00 AM - 09:00 AM', '08:00 AM - 09:00 AM'),
        ('09:00 AM - 10:00 AM', '09:00 AM - 10:00 AM'),
        ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
        ('11:00 AM - 12:00 AM', '11:00 AM - 12:00 AM'),
        ('01:00 PM - 02:00 PM', '01:00 PM - 02:00 PM'),
        ('02:00 PM - 03:00 PM', '02:00 PM - 03:00 PM'),
        ('03:00 PM - 04:00 PM', '03:00 PM - 04:00 PM')
    )
    TimeSlot  = forms.ChoiceField(required=True, choices = slots)
    class Meta:
        model = Appointments
        fields = ['DoctorUser', 'AppointmentDate', 'TimeSlot']
        widgets = { 
            'AppointmentDate': widgets.DateInput(attrs = { 'type': 'date' })
        }
        labels = {
            "AppointmentDate": "Appointment Date"
        }
        
    
    def __init__(self, *args, **kwargs):
        super(BookAppointmentForm, self).__init__(*args, **kwargs)
            
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control floating'

            if visible.field.widget.input_type == "select":
                visible.field.widget.attrs['class'] = "form-select form-control floating"
    

    

