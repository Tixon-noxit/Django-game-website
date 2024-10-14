from django.shortcuts import render
from django.templatetags.static import static
from . import models


def review_view(request):
    context = {
        'page_title': 'Game reviews',
        'page_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada '
                            'lorem maximus mauris scelerisque, at rutrum nulla dictum.',
        'background_image_url': static('img/page-top-bg/3.jpg'),
        'reviews': models.Reviews.objects.all(),
    }
    return render(request, 'review/review.html', context=context)
