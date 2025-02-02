from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.AppointmentListView.as_view(), name='appointment-list'),
    path('create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('<int:pk>/edit/', views.AppointmentUpdateView.as_view(), name='appointment-edit'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('<int:pk>/cancel/', views.cancel_appointment, name='appointment-cancel'),
    path('patient/<int:patient_id>/appointments/', 
         views.PatientAppointmentsView.as_view(), 
         name='patient-appointments'),
    path('patient/<int:patient_id>/create/', 
         views.PatientAppointmentCreateView.as_view(), 
         name='patient-appointment-create'),
    path('patient/<int:patient_id>/appointment/<int:pk>/edit/', 
         views.PatientAppointmentUpdateView.as_view(), 
         name='patient-appointment-edit'),
    path('doctor/<int:doctor_id>/appointments/', 
         views.DoctorAppointmentsView.as_view(), 
         name='doctor-appointments'),
]