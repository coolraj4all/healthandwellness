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
    path('passwordreset', views.password_reset, name='password_reset'),
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

    path('patients/', views.PatientViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='patients-list'),
    path('patients/<str:pk>/', views.PatientViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='patients-details'),

    path('doctors/', views.DoctorViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='doctors-list'),
    path('doctors/<str:pk>/', views.DoctorViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='doctors-details'),

    path('receptionists/', views.ReceptionistViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='receptionists-list'),
    path('receptionists/<str:pk>/', views.ReceptionistViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='receptionists-details'),

]