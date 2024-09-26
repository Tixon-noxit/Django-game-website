from django.urls import reverse
from index.models import News, Games
from forum.models import ForumPost


def main_menu_context(request):
    """main_menu"""
    main_menu = [
        {'title': 'Home', 'url': reverse('index')},
        {'title': 'Games', 'url': reverse('review')},
        {'title': 'Blog', 'url': reverse('blog')},
        {'title': 'Forums', 'url': reverse('forum')},
        {'title': 'Contact', 'url': reverse('contact')},
    ]
    return {'main_menu': main_menu}


def retutn_news(request):
    """news list"""
    return {'news': News.objects.all()}


def latest_posts(request):
    """latest posts """
    return {'latest_posts': Games.objects.all()[:3]}


def top_comments(request):
    """top comments """
    return {'top_comments': ForumPost.objects.all()[:4]}
