from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Engineer, Asset

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
