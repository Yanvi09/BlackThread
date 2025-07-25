import pytest
from core.models import Engineer, Asset, Mission, ThreatLog, ActivityLog

@pytest.mark.django_db
def test_create_engineer():
    engineer = Engineer.objects.create(name="Jane Doe", email="jane@example.com", specialty="AI Specialist")
    assert engineer.name == "Jane Doe"

@pytest.mark.django_db
def test_create_asset():
    asset = Asset.objects.create(name="Drone X", category="Aerial", status="Available")
    assert asset.status == "Available"

@pytest.mark.django_db
def test_create_mission():
    mission = Mission.objects.create(title="Recon", location="Sector 7", urgency="High", status="Planned")
    assert mission.title == "Recon"

@pytest.mark.django_db
def test_create_threat_log():
    mission = Mission.objects.create(title="Recon", location="Sector 7", urgency="High", status="Planned")
    threat = ThreatLog.objects.create(mission=mission, description="Hostile detected", level="Critical")
    assert threat.level == "Critical"

@pytest.mark.django_db
def test_create_activity_log():
    log = ActivityLog.objects.create(action="Asset Deployed")
    assert "Asset Deployed" in str(log)
