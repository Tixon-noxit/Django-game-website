"""
URL configuration for Django_game_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from review.views import review_view
from index.views import home_view
from blog.views import BlogListView
from forum.views import ForumListView
from contact.views import ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path('games/', review_view, name='review'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('forum/', ForumListView.as_view(), name='forum'),
    path('contact/', ContactView.as_view(), name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)