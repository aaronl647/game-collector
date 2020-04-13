from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Games, Platform
from .forms import PlayTimeForm

class GamesCreate(CreateView):
    model = Games
    fields = '__all__'
    success_url = '/games/'

class GamesUpdate(UpdateView):
    model = Games
    fields = ['name', 'genre']
    success_url = '/games/'

class GamesDelete(DeleteView):
    model = Games
    success_url = '/games/'

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Games.objects.all()
    return render(request, 'games/index.html', {'games': games})

def games_detail(request, games_id):
    game = Games.objects.get(id=games_id)
    games_not_on_platform = Platform.objects.exclude(id__in = game.platform.all().values_list('id'))
    playtime_form = PlayTimeForm()
    return render(request, 'games/detail.html', { 
        'game' : game, 
        'playtime_form': playtime_form,
        'platform': games_not_on_platform})

def add_playtime(request, games_id):
    form = PlayTimeForm(request.POST)
    if form.is_valid():
        new_playtime = form.save(commit=False)
        new_playtime.games_id = games_id
        new_playtime.save()
    return redirect('detail', games_id = games_id)

def assoc_platform(request, games_id, platform_id):
    Games.objects.get(id=games_id).platform.add(platform_id)
    return redirect('detail', games_id=games_id)