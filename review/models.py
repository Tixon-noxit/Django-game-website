from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Reviews(models.Model):
    """Reviews model"""
    title = models.CharField(max_length=255, verbose_name='title Reviews')
    text = models.TextField(verbose_name='text Reviews')
    rating = models.FloatField(validators=[
        MinValueValidator(0.0),
        MaxValueValidator(10.0),
    ], verbose_name='rating Reviews'
    )
    image = models.ImageField(upload_to='review_backgrounds/', verbose_name='image Reviews')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
