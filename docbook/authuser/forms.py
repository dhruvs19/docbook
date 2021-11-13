from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    USERS = (
        ('','You Are ?'),
        ('patient','Patient'),
        ('doctor','Doctor'),
    )
    userType = forms.ChoiceField(required=True, choices = USERS)

    class Meta:
        model = User
        fields=("userType","username","email", "password1","password2")
    
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control floating'

            if visible.field.widget.input_type == "select":
                visible.field.widget.attrs['class'] = "form-select form-control floating"
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user