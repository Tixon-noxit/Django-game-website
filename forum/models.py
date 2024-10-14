from django.db import models
from django.templatetags.static import static


class ForumPost(models.Model):
    """ForumPost models"""
    avatar = models.ImageField(upload_to='comment_images/', verbose_name='image ForumPost',
                               default=static('img/authors/8.jpg'))
    author = models.CharField(max_length=255, verbose_name='author ForumPost')
    content = models.TextField(verbose_name='text ForumPost')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return f"{self.author} - {self.content}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'ForumPost'
        verbose_name_plural = 'ForumPosts'


class ForumPostAttachment(models.Model):
    """Forum PostAttachment model"""

    post = models.ForeignKey(ForumPost, related_name='attachments', on_delete=models.CASCADE, verbose_name='Post')
    file = models.FileField(upload_to='attachments/', verbose_name='Attachment File')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Uploaded At')

    def __str__(self):
        return f"Attachment for {self.post.content}"

    class Meta:
        verbose_name = 'Post Attachment'
        verbose_name_plural = 'Post Attachments'


