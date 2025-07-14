from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EngineerForm, AssetForm, MissionForm, ThreatLogForm
from .models import Engineer, Asset, Mission, ThreatLog, ActivityLog
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Register view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

# Login view
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

# Logout view
def logout(request):
    auth_logout(request)
    return redirect('login')

# Dashboard with insights
@login_required
def dashboard(request):
    recent_missions = Mission.objects.order_by('-created_on')[:5]
    critical_threats = ThreatLog.objects.filter(level='Critical').order_by('-reported_on')[:3]
    recent_logs = ActivityLog.objects.order_by('-timestamp')[:10]

    context = {
        'missions': recent_missions,
        'critical_threats': critical_threats,
        'logs': recent_logs
    }
    return render(request, 'core/dashboard.html', context)

# Engineer CRUD
@login_required
def engineer_list(request):
    engineers = Engineer.objects.all()
    return render(request, 'core/engineer_list.html', {'engineers': engineers})

@login_required
def engineer_create(request):
    if request.method == 'POST':
        form = EngineerForm(request.POST)
        if form.is_valid():
            engineer = form.save()
            ActivityLog.objects.create(action=f"Engineer created: {engineer.name}")
            return redirect('engineer_list')
    else:
        form = EngineerForm()
    return render(request, 'core/engineer_form.html', {'form': form})

@login_required
def engineer_update(request, pk):
    engineer = get_object_or_404(Engineer, pk=pk)
    if request.method == 'POST':
        form = EngineerForm(request.POST, instance=engineer)
        if form.is_valid():
            engineer = form.save()
            ActivityLog.objects.create(action=f"Engineer updated: {engineer.name}")
            return redirect('engineer_list')
    else:
        form = EngineerForm(instance=engineer)
    return render(request, 'core/engineer_form.html', {'form': form})

@login_required
def engineer_delete(request, pk):
    engineer = get_object_or_404(Engineer, pk=pk)
    ActivityLog.objects.create(action=f"Engineer deleted: {engineer.name}")
    engineer.delete()
    return redirect('engineer_list')

# Asset CRUD
@login_required
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'core/asset_list.html', {'assets': assets})

@login_required
def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save()
            ActivityLog.objects.create(action=f"Asset created: {asset.name}")
            return redirect('asset_list')
    else:
        form = AssetForm()
    return render(request, 'core/asset_form.html', {'form': form})

@login_required
def asset_update(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            asset = form.save()
            ActivityLog.objects.create(action=f"Asset updated: {asset.name}")
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'core/asset_form.html', {'form': form})

@login_required
def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    ActivityLog.objects.create(action=f"Asset deleted: {asset.name}")
    asset.delete()
    return redirect('asset_list')

# Mission CRUD
@login_required
def mission_list(request):
    missions = Mission.objects.all()
    return render(request, 'core/mission_list.html', {'missions': missions})

@login_required
def mission_create(request):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            mission = form.save()
            ActivityLog.objects.create(action=f"Mission created: {mission.title}")
            return redirect('mission_list')
    else:
        form = MissionForm()
    return render(request, 'core/mission_form.html', {'form': form})

@login_required
def mission_update(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'POST':
        form = MissionForm(request.POST, instance=mission)
        if form.is_valid():
            mission = form.save()
            ActivityLog.objects.create(action=f"Mission updated: {mission.title}")
            return redirect('mission_list')
    else:
        form = MissionForm(instance=mission)
    return render(request, 'core/mission_form.html', {'form': form})

@login_required
def mission_delete(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    ActivityLog.objects.create(action=f"Mission deleted: {mission.title}")
    mission.delete()
    return redirect('mission_list')

# Threat Logs
@login_required
def threat_list(request):
    threats = ThreatLog.objects.all()
    return render(request, 'core/threat_list.html', {'threats': threats})

@login_required
def threat_create(request):
    if request.method == 'POST':
        form = ThreatLogForm(request.POST)
        if form.is_valid():
            threat = form.save()
            ActivityLog.objects.create(action=f"Threat reported for: {threat.mission.title}")
            return redirect('threat_list')
    else:
        form = ThreatLogForm()
    return render(request, 'core/threat_form.html', {'form': form})

@login_required
def threat_delete(request, pk):
    threat = get_object_or_404(ThreatLog, pk=pk)
    ActivityLog.objects.create(action=f"Threat removed from: {threat.mission.title}")
    threat.delete()
    return redirect('threat_list')

@login_required
def dashboard(request):
    recent_missions = Mission.objects.order_by('-created_on')[:5]
    critical_threats = ThreatLog.objects.filter(level='Critical').order_by('-reported_on')[:3]
    recent_logs = ActivityLog.objects.order_by('-timestamp')[:10]

    context = {
        'missions': recent_missions,
        'critical_threats': critical_threats,
        'logs': recent_logs
    }
    return render(request, 'core/dashboard.html', context)
