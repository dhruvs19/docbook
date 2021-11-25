from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import DocProfile


class DocProfileForm(ModelForm):
    GROUPS = (
        ('', 'Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),

    )

    gender = forms.ChoiceField(required=True, choices=GROUPS)

    class Meta:
        model = DocProfile
        fields = ['profile_image', 'name', 'gender', 'reg_clinic_address','pincode', 'age', 'bio', 'qualification', 'mobile']

    def __init__(self, *args, **kwargs):
        super(DocProfileForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control floating'

            if visible.field.widget.input_type == "select":
                visible.field.widget.attrs['class'] = "form-select form-control floating"
