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
        return f"{self.name} ({self.category})"
