from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [    
    # Add this new URL pattern
    path('search/', views.search_medicines, name='medicine-search'),
    
    # Template views for Manufacturer
    path('manufacturer/', views.ManufacturerListView.as_view(), name='manufacturer-list'),
    path('manufacturer/create/', views.ManufacturerCreateView.as_view(), name='manufacturer-create'),
    path('manufacturer/<int:pk>/', views.ManufacturerDetailView.as_view(), name='manufacturer-detail'),
    path('manufacturer/<int:pk>/update/', views.ManufacturerUpdateView.as_view(), name='manufacturer-update'),
    path('manufacturer/<int:pk>/delete/', views.ManufacturerDeleteView.as_view(), name='manufacturer-delete'),
    
    # Template views for Medicine
    path('medicine/', views.MedicineListView.as_view(), name='medicine-list'),
    path('medicine/create/', views.MedicineCreateView.as_view(), name='medicine-create'),
    path('medicine/<int:pk>/', views.MedicineDetailView.as_view(), name='medicine-detail'),
    path('medicine/<int:pk>/update/', views.MedicineUpdateView.as_view(), name='medicine-update'),
    path('medicine/<int:pk>/delete/', views.MedicineDeleteView.as_view(), name='medicine-delete'),
    
    # Template views for Brand
    path('brand/', views.BrandListView.as_view(), name='brand-list'),
    path('brand/create/', views.BrandCreateView.as_view(), name='brand-create'),
    path('brand/<int:pk>/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('brand/<int:pk>/update/', views.BrandUpdateView.as_view(), name='brand-update'),
    path('brand/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand-delete'),
]

