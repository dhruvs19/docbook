from django.urls import path,include
from .views import *
from . import views
app_name = 'core'

urlpatterns = [
    path('', HomepageView.as_view(), name="home"),
    
]