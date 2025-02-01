from django.urls import path
from . import views
app_name = 'medicines'


urlpatterns = [
    path('manufacturers/', views.ManufacturerViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='manufacturers-list'),
    path('manufacturers/<str:pk>/', views.ManufacturerViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='manufacturers-details'),
    path('medicines/', views.MedicineViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='medicines-list'),
    path('medicines/<str:pk>/', views.MedicineViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='medicines-details'),
    path('brands/', views.BrandViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='brands-list'),
    path('brands/<str:pk>/', views.BrandViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='brands-details'),
    path('recommendations/', views.MedicineRecommendationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='recommendations-list'),
    path('recommendations/<str:pk>/', views.MedicineRecommendationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='recommendations-details'),
]

