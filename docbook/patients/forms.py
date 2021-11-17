from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Patients


class PatientsForm(ModelForm):
    GROUPS = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    BloodGroup = forms.ChoiceField(required=True, choices = GROUPS)

    class Meta:
        model = Patients
        fields = ['FirstName', 'LastName', 'Address', 'PhoneNumber', 'DOB', 'BloodGroup']
    
    def __init__(self, *args, **kwargs):
        super(PatientsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control floating'

            if visible.field.widget.input_type == "select":
                visible.field.widget.attrs['class'] = "form-select form-control floating"
    
    def save(self, commit=True):
        patient = super(PatientsForm, self).save(commit=False)
        if commit:
            patient.save()
        return patient
        