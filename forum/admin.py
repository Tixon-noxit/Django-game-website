from django.contrib import admin
from . import models

admin.site.register(models.ForumPost)
admin.site.register(models.ForumPostAttachment)
