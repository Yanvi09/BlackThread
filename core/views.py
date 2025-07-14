from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

from .forms import RegisterForm, EngineerForm, AssetForm
from .models import Engineer, Asset


from .models import Mission, ThreatLog
from .forms import MissionForm, ThreatLogForm

# User Register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

# User Login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

# Logout
def logout(request):
    auth_logout(request)
    return redirect('login')

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

# =============================
# ENGINEERS
# =============================

@login_required
def engineer_list(request):
    engineers = Engineer.objects.all()
    return render(request, 'core/engineer_list.html', {'engineers': engineers})

@login_required
def engineer_create(request):
    form = EngineerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('engineer_list')
    return render(request, 'core/engineer_form.html', {'form': form})

@login_required
def engineer_update(request, pk):
    engineer = Engineer.objects.get(pk=pk)
    form = EngineerForm(request.POST or None, instance=engineer)
    if form.is_valid():
        form.save()
        return redirect('engineer_list')
    return render(request, 'core/engineer_form.html', {'form': form})

@login_required
def engineer_delete(request, pk):
    engineer = Engineer.objects.get(pk=pk)
    engineer.delete()
    return redirect('engineer_list')

# =============================
# ASSETS
# =============================

@login_required
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'core/asset_list.html', {'assets': assets})

@login_required
def asset_create(request):
    form = AssetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('asset_list')
    return render(request, 'core/asset_form.html', {'form': form})

@login_required
def asset_update(request, pk):
    asset = Asset.objects.get(pk=pk)
    form = AssetForm(request.POST or None, instance=asset)
    if form.is_valid():
        form.save()
        return redirect('asset_list')
    return render(request, 'core/asset_form.html', {'form': form})

@login_required
def asset_delete(request, pk):
    asset = Asset.objects.get(pk=pk)
    asset.delete()
    return redirect('asset_list')


@login_required
def mission_list(request):
    missions = Mission.objects.all()
    return render(request, 'core/mission_list.html', {'missions': missions})

@login_required
def mission_create(request):
    form = MissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mission_list')
    return render(request, 'core/mission_form.html', {'form': form})

@login_required
def mission_update(request, pk):
    mission = Mission.objects.get(pk=pk)
    form = MissionForm(request.POST or None, instance=mission)
    if form.is_valid():
        form.save()
        return redirect('mission_list')
    return render(request, 'core/mission_form.html', {'form': form})

@login_required
def mission_delete(request, pk):
    Mission.objects.get(pk=pk).delete()
    return redirect('mission_list')

# =============================
# THREAT LOGS
# =============================

@login_required
def threat_list(request):
    threats = ThreatLog.objects.all()
    return render(request, 'core/threat_list.html', {'threats': threats})

@login_required
def threat_create(request):
    form = ThreatLogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('threat_list')
    return render(request, 'core/threat_form.html', {'form': form})

@login_required
def threat_delete(request, pk):
    ThreatLog.objects.get(pk=pk).delete()
    return redirect('threat_list')
