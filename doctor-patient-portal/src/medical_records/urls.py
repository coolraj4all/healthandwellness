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
    path('medicine-details/', views.PatientMedicineDetailsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='medicine-details-list'),
    path('medicine-details/create/', views.PatientMedicineDetailsViewSet.as_view({
        'get': 'create',
        'post': 'create'
    }), name='medicine-details-create'),
    path('medicine-details/<int:pk>/update/', views.PatientMedicineDetailsViewSet.as_view({
        'get': 'update',
        'post': 'update'
    }), name='medicine-details-update'),
    path('medicine-details/<int:pk>/delete/', views.PatientMedicineDetailsViewSet.as_view({
        'post': 'destroy'
    }), name='medicine-details-delete'),

    path('patient-health/<int:pk>/pdf/', 
         views.PatientMedicationViewSet.as_view({'get': 'generate_pdf'}), 
         name='patient-health-pdf'),
]