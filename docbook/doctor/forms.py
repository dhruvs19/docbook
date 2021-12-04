from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets, DateField
from django.forms import ModelForm

from appointments.models import Appointments
from .models import *


class DocProfileForm(forms.ModelForm):
    GROUPS = (
        ('','Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),

    )
    GROUPS_S = (
        ('','Specialization'),
        ('Cardiologist', 'Cardiologist'),
        ('Neurologist', 'Neurologist'),
        ('Gynaecologist','Gynaecologist')
    )

    GROUPS_L = (
        ('','Location'),
        ('Ontario(ON)', 'Ontario(ON)'),
        ('Quebec(QC)', 'Quebec(QC)'),
        ('Alberta(AB)','Alberta(AB)'),
    )

    gender = forms.ChoiceField(required=True, choices = GROUPS)
    specialization = forms.ChoiceField(required=True, choices = GROUPS_S)
    location = forms.ChoiceField(required=True, choices = GROUPS_L)

    class Meta:
        model = DocProfile
        fields = ['profile_image','name', 'gender', 'reg_clinic_address', 'pincode','location', 'age','bio','qualification','specialization','mobile']
        widgets = {
            'profile_image': widgets.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DocProfileForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control floating'

            if visible.field.widget.input_type == "select":
                visible.field.widget.attrs['class'] = "form-select form-control floating"


