from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets, DateField
from .models import Patients


class PatientsForm(ModelForm):
    GROUPS = (
        ('','Blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    BloodGroup  = forms.ChoiceField(required=True, choices = GROUPS)
    class Meta:
        model = Patients
        fields = ['ProfilePicture', 'FirstName', 'LastName', 'Address', 'PhoneNumber', 'DOB', 'BloodGroup']
        widgets = { 
            'DOB': widgets.DateInput(attrs = { 'type': 'date' }),
            'ProfilePicture': widgets.FileInput(),
        }
        labels = {
            "ProfilePicture": "Change Profile Picture",
            "FirstName": "First Name",
            "LastName": "Last Name",
            "Phonenumber": "Phone number",
            "DOB": "Date of Birth",
            "BloodGroup": "Select Blood Group"
        }
        
    
    def __init__(self, *args, **kwargs):
        super(PatientsForm, self).__init__(*args, **kwargs)
            
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control floating'

            if visible.field.widget.input_type == "select":
                visible.field.widget.attrs['class'] = "form-select form-control floating"
    

        