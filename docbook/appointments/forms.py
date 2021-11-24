from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets, DateField
from .models import Appointments
from patients.models import Patients
from doctor.models import DocProfile


class BookAppointmentForm(ModelForm):
    # doctor_objs = DocProfile.objects.all()

    # DOCLIST = [('','Select Doctor')]
    # for each_obj in doctor_objs:
    #     # add specilisation later
    #     doc_tuple = (each_obj.UserID_id, "Dr. "+each_obj.name)
    #     DOCLIST.append(doc_tuple)
    # DoctorUser  = forms.ChoiceField(required=True, choices = tuple(DOCLIST))
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
    

