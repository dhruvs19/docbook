from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomepageView.as_view()),
]