from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Engineer, Asset
from .models import Mission, ThreatLog

# 🔐 Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# 🧑‍🔧 Engineer Form
class EngineerForm(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = '__all__'

# 🛰️ Asset Form
class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

# AssetForm
class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = '__all__'

# ThreatLogForm
class ThreatLogForm(forms.ModelForm):
    class Meta:
        model = ThreatLog
        fields = '__all__'