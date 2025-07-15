import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Engineer, Asset, Mission, ThreatLog

fake = Faker()


# ENGINEERS (Cybersecurity Personnel)
specialties = [
    'Network Forensics', 'Payload Reverse Engineering',
    'Threat Intelligence', 'Firewall Configuration',
    'Zero-Day Analysis', 'Red Team Ops', 'SIEM Monitoring'
]

for _ in range(10):
    Engineer.objects.create(
        name=fake.name(),
        email=fake.email(),
        specialty=random.choice(specialties),
        active=random.choice([True, False])
    )

#  ASSETS (StarkTech Gear / Modules)
categories = [
    'Quantum Firewall', 'AI Recon Drone', 'NanoCore Implant',
    'StarkVPN Node', 'Encryption Engine', 'Pulse Shield', 'EMP Toolkit'
]
statuses = ['Available', 'Deployed', 'Under Repair']
engineers = list(Engineer.objects.all())

for _ in range(15):
    Asset.objects.create(
        name=f"{fake.color_name()} {random.choice(categories)}",
        category=random.choice(categories),
        assigned_to=random.choice(engineers),
        status=random.choice(statuses)
    )


# MISSIONS (Security Deployments / Counter Ops)
urgencies = ['Low', 'Medium', 'High', 'Critical']
statuses = ['Planned', 'Ongoing', 'Completed']
assets = list(Asset.objects.all())

for _ in range(10):
    mission = Mission.objects.create(
        title=fake.catch_phrase(),
        location=fake.city(),
        urgency=random.choice(urgencies),
        status=random.choice(statuses),
    )
    mission.assigned_engineers.set(random.sample(engineers, k=2))
    mission.assets_used.set(random.sample(assets, k=2))

# THREATS (Live Threat Reports)
threat_levels = ['Info', 'Caution', 'Severe', 'Critical']
missions = list(Mission.objects.all())

for _ in range(30):
    ThreatLog.objects.create(
        mission=random.choice(missions),
        description=fake.sentence(nb_words=12),
        level=random.choice(threat_levels)
    )

print("  fake data loaded successfully!")
