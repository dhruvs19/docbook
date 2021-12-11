from os import name
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
app_name = 'authuser'

urlpatterns = [
    path('login/', LoginPage.as_view(), name="login_url"),
    path('register/', RegisterPage.as_view(), name="register_url"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_url')
]