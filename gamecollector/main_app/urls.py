from django.urls import path
from .views import home, about, games_index, games_detail, add_playtime, assoc_platform, unassoc_platform, signup, GamesCreate, GamesUpdate, GamesDelete

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('games/', games_index, name='index'),
    path('games/<int:games_id>/', games_detail, name='detail'),
    path('games/<int:games_id>/add_playtime/', add_playtime, name='add_playtime'),
    path('games/<int:games_id>/assoc_platform/<int:platform_id>/', assoc_platform, name='assoc_platform'),
    path('games/<int:games_id>/unassoc_platform/<int:platform_id>/', unassoc_platform, name='unassoc_platform'),

    path('games/create/', GamesCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update', GamesUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete', GamesDelete.as_view(), name='games_delete'),
    path('accounts/signup/', signup, name='signup'),
]