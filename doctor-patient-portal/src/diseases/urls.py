from django.urls import path
from . import views

app_name = 'diseases'
urlpatterns = [
    # Disease Category URLs
    path('categories/', views.DiseaseCategoryViewSet.as_view({'get': 'list'}), name='category-list'),
    path('categories/create/', views.DiseaseCategoryViewSet.as_view({'get': 'create', 'post': 'create'}), name='category-create'),
    path('categories/<int:pk>/', views.DiseaseCategoryViewSet.as_view({'get': 'retrieve'}), name='category-detail'),
    path('categories/<int:pk>/update/', views.DiseaseCategoryViewSet.as_view({'get': 'update', 'post': 'update'}), name='category-update'),
    path('categories/<int:pk>/delete/', views.DiseaseCategoryViewSet.as_view({'get': 'destroy', 'post': 'destroy'}), name='category-delete'),

    # Disease URLs
    path('diseases/', views.DiseaseViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='disease-list'),
    path('diseases/<str:pk>/', views.DiseaseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='disease-detail'),
]