from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse

class LoginPage(LoginView):
    template_name = 'auth/login.html'

class LoginSuccess(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return redirect(reverse("admin:index"))
        else:
            return redirect("core:home")
