from django.urls import path
from .views import *

urlpatterns = [
    path('team/',TeamView.as_view(),name='team'),
    path('team_detail/<int:pk>',TeamDetailView.as_view(),name='team_detail'),
    path('player/',PlayerListCreateView.as_view(),name='player'),
    path('player_history/',PlayerStatsView.as_view(),name='player_history'),   
    path('player_history_detail/<int:pk>',PlayerStatsDetailView.as_view(),name='player_history_detail'),
    path('player_detail/<int:pk>',PlayerDetailView.as_view(),name='player_detail'),
    path('match/',MatchScheduleView.as_view(),name='match'),
    path('match_result/',MatchResultView.as_view(),name='match_result'),
    path('points/',PointsTableView.as_view(),name='points'),    
]