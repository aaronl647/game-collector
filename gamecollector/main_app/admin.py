from django.contrib import admin

from .models import Games, PlayTime, Platform, Photo
# Register your models here.

admin.site.register(Games)
admin.site.register(PlayTime)
admin.site.register(Platform)
admin.site.register(Photo)