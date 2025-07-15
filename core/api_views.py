from rest_framework import viewsets, permissions
from .models import Engineer, Asset, Mission, ThreatLog
from .serializers import (
    EngineerSerializer, AssetSerializer, MissionSerializer, ThreatLogSerializer
)
from rest_framework.authentication import TokenAuthentication

class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class ThreatLogViewSet(viewsets.ModelViewSet):
    queryset = ThreatLog.objects.all()
    serializer_class = ThreatLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
