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
    path('diseases/', views.DiseaseViewSet.as_view({'get': 'list'}), name='disease-list'),
    path('diseases/create/', views.DiseaseViewSet.as_view({'get': 'create', 'post': 'create'}), name='disease-create'),
    path('diseases/<int:pk>/', views.DiseaseViewSet.as_view({'get': 'retrieve'}), name='disease-detail'),
    path('diseases/<int:pk>/update/', views.DiseaseViewSet.as_view({'get': 'update', 'post': 'update'}), name='disease-update'),
    path('diseases/<int:pk>/delete/', views.DiseaseViewSet.as_view({'get': 'destroy', 'post': 'destroy'}), name='disease-delete'),
]