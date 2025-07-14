from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('engineers/', views.engineer_list, name='engineer_list'),
    path('engineers/create/', views.engineer_create, name='engineer_create'),
    path('engineers/<int:pk>/edit/', views.engineer_update, name='engineer_update'),
    path('engineers/<int:pk>/delete/', views.engineer_delete, name='engineer_delete'),

    path('assets/', views.asset_list, name='asset_list'),
    path('assets/create/', views.asset_create, name='asset_create'),
    path('assets/<int:pk>/edit/', views.asset_update, name='asset_update'),
    path('assets/<int:pk>/delete/', views.asset_delete, name='asset_delete'),
]
