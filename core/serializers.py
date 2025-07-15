from rest_framework import serializers
from .models import Engineer, Asset, Mission, ThreatLog

class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class ThreatLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatLog
        fields = '__all__'
