from django.urls import path
from . import views


urlpatterns = [
    path('about', views.about, name='about'),
    path('Games', views.CRUD_Games, name='GameList'),
    path('', views.homepage, name='homepage'),
    path('Games/add_games', views.add_game, name='add_game'),
    path('Games/<int:game_id>/update', views.update_game, name='game_update'),
    path('game/delete/<int:game_id>/', views.game_delete, name='game_delete'),
    
]