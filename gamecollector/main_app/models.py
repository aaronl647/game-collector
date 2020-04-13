from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

YESNO = (
    ('Y', 'Yes'),
    ('N', 'No')
)

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=20)
    developer = models.CharField(max_length=20)
    generation = models.IntegerField(default=1)
    release_year = models.IntegerField(default=1980)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('platform_detail', kwargs={'pk': self.id})

class Games(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    platform = models.ManyToManyField(Platform)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'games_id': self.id})

class PlayTime(models.Model):
    date = models.DateField(('Date'), default=date.today)
    hours_played = models.IntegerField(default=0)
    completed = models.CharField(
        max_length=1,
        choices=YESNO,
        default=YESNO[1]
        )
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_completed_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


