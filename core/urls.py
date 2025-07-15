from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import EngineerViewSet, AssetViewSet, MissionViewSet, ThreatLogViewSet
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'api/engineers', EngineerViewSet)
router.register(r'api/assets', AssetViewSet)
router.register(r'api/missions', MissionViewSet)
router.register(r'api/threats', ThreatLogViewSet)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


    path('engineers/', views.engineer_list, name='engineer_list'),
    path('engineers/create/', views.engineer_create, name='engineer_create'),
    path('engineers/<int:pk>/edit/', views.engineer_update, name='engineer_update'),
    path('engineers/<int:pk>/delete/', views.engineer_delete, name='engineer_delete'),

    path('assets/', views.asset_list, name='asset_list'),
    path('assets/create/', views.asset_create, name='asset_create'),
    path('assets/<int:pk>/edit/', views.asset_update, name='asset_update'),
    path('assets/<int:pk>/delete/', views.asset_delete, name='asset_delete'),

    path('missions/', views.mission_list, name='mission_list'),
    path('missions/create/', views.mission_create, name='mission_create'),
    path('missions/<int:pk>/edit/', views.mission_update, name='mission_update'),
    path('missions/<int:pk>/delete/', views.mission_delete, name='mission_delete'),

    path('threats/', views.threat_list, name='threat_list'),
    path('threats/create/', views.threat_create, name='threat_create'),
    path('threats/<int:pk>/delete/', views.threat_delete, name='threat_delete'),

    path('', include(router.urls)), 
]
