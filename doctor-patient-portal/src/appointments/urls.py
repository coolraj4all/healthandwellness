from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.AppointmentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('appointments/<str:pk>/', views.AppointmentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]