from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_page(request):
    form = Loginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:  # User exists
                login(request, user)
                return redirect('index')
            else:  # User does not exist, redirect to register page
                messages.error(request, 'User does not exist. Please register.')
                return redirect('login')
        else:
            messages.error(request,'error validating form')
            return redirect('login')
    return render(request,'Users/login.html',{'form':form})

def profile_logout(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request,'index.html')

def players(request):
    player_list = Player.objects.all()
    context = {
        'players': player_list
    }
    return render(request,'players.html',context)

def players_details(request,player_id):
    player = get_object_or_404(Player,pk=player_id)
    context = {
        'player':player
    }
    return render(request,'player_details.html',context)

def all_team(request):
    teams = Team.objects.all()
    context = {
        'team':teams
    }
    return render(request,'team.html',context)

def team_details(request,team_id):
    team_ = get_object_or_404(Team,pk=team_id)
    players = Player.objects.filter(team=team_)
    print(players)
    context = {
        'team':team_,
        'players':players
    }
    return render(request,'team_details.html',context)

from .forms import SoldForm

def sell_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        form = SoldForm(request.POST, player=player)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except ValueError as e:
                form.add_error(None, str(e))
    else:
        form = SoldForm(player=player)
    return render(request, 'bidding.html', {'form': form, 'player': player})

def search_home(request):
    all_players = Player.objects.all()
    form = PlayerIDSearchForm(request.GET or None)    
    if form.is_valid():
        player_id = form.cleaned_data['player_id']
        return redirect('search_results', player_id=player_id)
    return render(request, 'search.html', {'form': form,'all_players':all_players})

def search_results(request, player_id):
    all_players = Player.objects.all()
    form = PlayerIDSearchForm(request.GET or None)
    player = get_object_or_404(Player, id=player_id)
    if form.is_valid():
        new_player_id = form.cleaned_data['player_id']
        return redirect('search_results', player_id=new_player_id)
    return render(request, 'result.html', {'form': form, 'player': player,'all_players':all_players})