from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Games, Platform, Photo
from .forms import PlayTimeForm
import uuid
import boto3 

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'aaron-gametracker'


class GamesCreate(CreateView):
    model = Games
    fields = ['name', 'developer', 'publisher', 'genre', 'release_year']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GamesUpdate(UpdateView):
    model = Games
    fields = ['name', 'genre']
    success_url = '/games/'


class GamesDelete(DeleteView):
    model = Games
    success_url = '/games/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def games_index(request):
    games = Games.objects.filter(user=request.user)
    return render(request, 'games/index.html', {'games': games})

@login_required
def games_detail(request, games_id):
    game = Games.objects.get(id=games_id)
    games_not_on_platform = Platform.objects.exclude(id__in = game.platform.all().values_list('id'))
    playtime_form = PlayTimeForm()
    return render(request, 'games/detail.html', { 
        'game' : game, 
        'playtime_form': playtime_form,
        'platform': games_not_on_platform})

@login_required
def add_playtime(request, games_id):
    form = PlayTimeForm(request.POST)
    if form.is_valid():
        new_playtime = form.save(commit=False)
        new_playtime.games_id = games_id
        new_playtime.save()
    return redirect('detail', games_id = games_id)

@login_required
def assoc_platform(request, games_id, platform_id):
    Games.objects.get(id=games_id).platform.add(platform_id)
    return redirect('detail', games_id=games_id)

@login_required
def unassoc_platform(request, games_id, platform_id):
    Games.objects.get(id=games_id).platform.remove(platform_id)
    return redirect('detail', games_id=games_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def add_photo(request, games_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]        
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, games_id = games_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', games_id = games_id)

