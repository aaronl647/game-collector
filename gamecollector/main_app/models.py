from django.db import models
from django.urls import reverse

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    release_year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'games_id': self.id})