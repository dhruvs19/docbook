from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.template.response import TemplateResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

class LoginPage(LoginView):
    template_name = 'auth/login.html'

class LoginSuccess(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return redirect(reverse("admin:index"))
            else:
                return redirect(reverse("core:home"))
        else:
            return redirect(reverse("core:home"))

class RegisterPage(View):
    template_name = "auth/register.html"

    # get request to register page
    def get(self, *args, **kwargs):
        
        # redirect to homepage if already logged in
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return redirect("admin:index")
        else:
            # else show the register page
            context={
                "body_class":"account-page",
                "register_form":NewUserForm()}
            return(TemplateResponse(self.request, self.template_name, context))
    
    # post request to register page when user submits registration form
    def post(self, *args, **kwargs):
        form = NewUserForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            login(self.request, user)
            messages.success(self.request, "Registration successful." )
            return redirect("core:home")
        context={
                "body_class":"account-page",
                "register_form":form}
        messages.error(self.request, "Unsuccessful registration. Invalid information.")
        return(TemplateResponse(self.request, self.template_name, context))
        