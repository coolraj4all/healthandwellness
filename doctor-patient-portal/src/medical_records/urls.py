from django.urls import path
from . import views
app_name = 'records'
urlpatterns = [
    path('health/', views.PatientMedicationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='patient-health-list'),
    path('health/create/', views.PatientMedicationViewSet.as_view({
        'get': 'create',
        'post': 'create'
    }), name='patient-health-create'),
    path('health/<int:pk>/', views.PatientMedicationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='patient-health-detail'),
    path('health/<int:pk>/update/', views.PatientMedicationViewSet.as_view({
        'get': 'retrieve',
        'post': 'update'
    }), name='patient-health-update'),
]