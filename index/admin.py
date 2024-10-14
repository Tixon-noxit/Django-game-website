from django.contrib import admin
from . import models

admin.site.register(models.GamesGenre)
admin.site.register(models.Games)
admin.site.register(models.Tournaments)
admin.site.register(models.News)
