from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=20)
    developer = models.CharField(max_length=20)
    generation = models.IntegerField()
    release_year = models.DateField()
    
    def __str__(self):
        return self.name

class Games(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    hours_played = models.IntegerField(default=0)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    platform = models.ManyToManyField(Platform) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'games_id': self.id})

