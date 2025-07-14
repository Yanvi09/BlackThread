from django.db import models
from django.contrib.auth.models import User

class Engineer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialty = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(Engineer, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('Available', 'Available'),
        ('Deployed', 'Deployed'),
        ('Under Repair', 'Under Repair')
    ])
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Mission(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    urgency = models.CharField(max_length=20, choices=[
        ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')
    ])
    status = models.CharField(max_length=20, choices=[
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ])
    assigned_engineers = models.ManyToManyField(Engineer, blank=True)
    assets_used = models.ManyToManyField(Asset, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ThreatLog(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=[
        ('Info', 'Info'),
        ('Caution', 'Caution'),
        ('Severe', 'Severe'),
        ('Critical', 'Critical'),
    ])
    reported_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.level} Threat - {self.mission.title}"

class ActivityLog(models.Model):
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} at {self.timestamp}"
