from django import forms
from .forms import NewUserForm
from django.contrib import messages
from doctor.models import DocProfile
from patients.models import Patients
from django.views.generic import View, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render, reverse
from django.template.response import TemplateResponse

# Custom login form to Override default django AuthenticationForm
# and check if the user is active/inactive
class CustomLoginForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        self.error_messages['inactive'] = "This Account is inactive, \
            If you have recently registered, we will verify your account \
            before activating it. Thanks!"
        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None

                if user_temp is not None:
                        self.confirm_login_allowed(user_temp)
                else:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        params={'username': self.username_field.verbose_name},
                    )

        return self.cleaned_data

class LoginPage(LoginView):
    template_name = 'auth/login.html'
    authentication_form = CustomLoginForm

    # redirect after logging in as per the user role
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return reverse("admin:index")
            elif user.groups.filter(name='doctor').exists(): 
                return reverse("core:home")
            elif user.groups.filter(name='patient').exists():
                return reverse("patients:dashboard")
        return super().get_success_url()

class RegisterPage(View):
    template_name = "auth/register.html"

    # get request to register page
    def get(self, *args, **kwargs):
        
        # redirect to homepage if already logged in
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return redirect("admin:index")

        # else show the register page
        else:
            context={
                "body_class":"account-page",
                "register_form":NewUserForm()
            }
            return(TemplateResponse(self.request, self.template_name, context))
    
    # post request to register page when user submits registration form
    def post(self, *args, **kwargs):
        form = NewUserForm(self.request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)

            # if the user registered as a doctor, then:
                # 1. set the status as inactive (user moderation)
                # 2. add user to the doctor group
                # 3. make a row in DocProfile model for their personal details
            if form.cleaned_data['userType'] == 'doctor':
                user.is_active = False
                user.save()
                user.groups.add(Group.objects.get(name='doctor'))
                new_doc = DocProfile.objects.create(UserID = user)
                new_doc.save()
                messages.success(
                     self.request, 
                     "Registration successful. we will activate your \
                      account soon after we complete verifying it"
                    )

            # if the user registered as a patient, then:
                # 1. Add user to the patient group
                # 2. make a row in Patient model for their personal details
            elif form.cleaned_data['userType'] == 'patient':
                user.save()
                user.groups.add(Group.objects.get(name='patient'))
                new_patient = Patients.objects.create(UserID = user)
                new_patient.save()
                # login the user after registration
                login(self.request, user)
                messages.success(self.request, "Registration successful." )
            return redirect("core:home")
        
        # user registration failed, setting error msg
        else:
            messages.error(self.request, "Registration wasn't Successful, Please try again!!")
        
        context={
            "body_class":"account-page",
            "register_form":form
        }
        return(TemplateResponse(self.request, self.template_name, context))
        