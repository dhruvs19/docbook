
from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomepageView.as_view(), name="home"),
    path('about-us/', AboutPage.as_view(), name="about-us"),
    path('contact-us/', ContactPage.as_view(), name="contact-us")
]