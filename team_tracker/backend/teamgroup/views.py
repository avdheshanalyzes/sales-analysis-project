from django.shortcuts import render, get_object_or_404
from .models import Team, Member

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teamgroup/team_list.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    members = Member.objects.filter(team=team)
    return render(request, 'teamgroup/team_detail.html', {'team': team, 'members': members})
from django.shortcuts import render, get_object_or_404
from .models import Team, Member

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    members = Member.objects.filter(team=team)
    return render(request, 'teamgroup/team_detail.html', {'team': team, 'members': members})
