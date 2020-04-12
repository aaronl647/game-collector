from django.contrib import admin

from .models import Games, Platform
# Register your models here.

admin.site.register(Games)

admin.site.register(Platform)