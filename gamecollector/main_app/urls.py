from django.urls import path
from .views import home, about, games_index, games_detail, GamesCreate, GamesUpdate, GamesDelete

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('games/', games_index, name='index'),
    path('games/<int:games_id>/', games_detail, name='detail'),
    path('games/create/', GamesCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update', GamesUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete', GamesDelete.as_view(), name='games_delete'),
    
]