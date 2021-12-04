from os import name
from django.urls import path,re_path
from django.conf import settings
from .views  import *
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('accept/<int:pk>', views.acceptView, name = "accept-view"),
    path('view-app/', ViewApp.as_view(), name = "ap-list"),
    path('profile/', ProfileView.as_view(), name = "profile-view"),
    path('patient-list/', PatientListView.as_view(), name = "accept-view"),
    path('rej-patient-list/', PatientRejListView.as_view(), name = "reject-view"),
    path('update/<int:pk>', UpdateDoctorView.as_view(),name = "doctor-register"),
    path('delete/<int:pk>', views.deleteView, name = "delete-view"),
    #path('app-details/<str:appointment_id>', views.appDetails , name = "ap-details"),
    re_path(r'^app-details/(?P<appointment_id>\w{0,50})/$', views.appDetails, name = "ap-details"),
    re_path('update-appointment/', views.updateAppointment, name = "update-ap"),
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
