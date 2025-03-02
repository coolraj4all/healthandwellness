from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile-edit'),
    path('profile/password/', views.password_change, name='password-change'),
    path('passwordreset', views.password_reset, name='password_reset'),

    # User management URLs - put these before the viewset URLs
    path('users/list/', views.user_list, name='user-list'),
    path('users/<int:user_id>/change-password/', views.change_user_password, name='change-user-password'),

    # API viewset URLs
    path('users/', views.UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='users-list'),
    path('users/<str:pk>/', views.UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='users-details'),

    path('usertypes/', views.UserTypeViewSet.as_view({
        'get': 'list',
    }), name='usertypes-list'),
    path('usertypes/<str:pk>/', views.UserTypeViewSet.as_view({
        'get': 'retrieve',
    }), name='usertypes-details'),

    path('patients/list/', views.patient_list, name='patient-list'),
    path('patients/add/', views.patient_create, name='patient-create'),
    path('patients/<int:pk>/', views.patient_detail, name='patient-detail'),
    path('patients/<int:pk>/edit/', views.patient_edit, name='patient-edit'),

    path('doctors/list/', views.doctor_list, name='doctor-list'),
    path('doctors/add/', views.doctor_create, name='doctor-create'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor-detail'),
    path('doctors/<int:pk>/edit/', views.doctor_edit, name='doctor-edit'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor-delete'),
    path('doctors/<int:pk>/convert-to-user/', views.doctor_to_user, name='doctor-to-user'),
]