from django.urls import path
from games import views

urlpatterns = [
    path('game-categories/', views.GameCategoryList.as_view(), name=views.GameCategoryList.name),
    path('game-categories/<int:pk>/', views.GameCategoryDetail.as_view(), name=views.GameCategoryDetail.name),
    path('games/<int:pk>/', views.GameDetail.as_view(), name=views.GameDetail.name),
    path('games/', views.GameList.as_view(), name=views.GameList.name),
    path('players/', views.PlayerList.as_view(), name=views.PlayerList.name),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
    path('player-scores/', views.PlayerScoreList.as_view(), name=views.PlayerScoreList.name),
    path('player-scores/<int:pk>/', views.PlayerScoreDetail.as_view(), name=views.PlayerScoreDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

]
