from django.shortcuts import render
from . import models
from review.models import Reviews


def home_view(request):
    context = {
        'recent_games': models.Games.objects.all(),
        'tournament_games': models.Tournaments.objects.all(),
        'reviews': Reviews.objects.all(),
    }
    return render(request, 'index/index.html', context=context)
