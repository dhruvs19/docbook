from os import name
from django.urls import path
from django.conf import settings
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'patients'
urlpatterns = [

    path('', Profile_submit.as_view(), name="doctor-register")

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
