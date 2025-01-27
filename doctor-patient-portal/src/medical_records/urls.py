from django.urls import path
from . import views

urlpatterns = [
    path('medical-histories/', views.PatientMedicalHistoryViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('medical-histories/<str:pk>/', views.PatientMedicalHistoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('surgical-histories/', views.PatientSurgicalHistoryViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('surgical-histories/<str:pk>/', views.PatientSurgicalHistoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('medications/', views.PatientMedicationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('medications/<str:pk>/', views.PatientMedicationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]