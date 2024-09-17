from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login_page,name='login'),
    path('logout',views.profile_logout,name='logout'),
    path('',views.index,name='index'),
    path('players/',views.players,name='players'),
    path('player/<int:player_id>/',views.players_details,name='players_details'),
    path('teams/',views.all_team,name='team'),
    path('team/<int:team_id>/',views.team_details,name='team_details'),  
    path('sales/<int:player_id>/',views.sell_player,name='sales'),  
    path('search/', views.search_home, name='search-player'),
    path('results/<int:player_id>/', views.search_results, name='search_results'),
]