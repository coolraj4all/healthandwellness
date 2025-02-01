from django.urls import path
from . import views

app_name = 'diseases'
urlpatterns = [
    path('diseases/', views.DiseaseViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='disease-list'),
    path('diseases/<str:pk>/', views.DiseaseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='disease-detail'),

    path('diseasescategory/', views.DiseaseCategoryViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='disease-category-list'),
    path('diseasescategory/<str:pk>/', views.DiseaseCategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='disease-category-detail'),
]