from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Games

class GamesCreate(CreateView):
    model = Games
    fields = '__all__'
    success_url = '/games/'

class GamesUpdate(UpdateView):
    model = Games
    fields = ['name', 'developer', 'publisher', 'platform']

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
    return render(request, 'games/detail.html', { 'game' : game })