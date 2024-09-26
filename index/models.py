from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class GamesGenre(models.Model):
    """Recent game genre model"""
    name = models.CharField(max_length=255, verbose_name='name Recent')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Games(models.Model):
    """Recent game model"""
    title = models.CharField(max_length=255, verbose_name='title Recent')
    genre = models.ForeignKey(GamesGenre, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Recent game genre')
    text = models.TextField(verbose_name='text Recent')
    image = models.ImageField(upload_to='games_backgrounds/', verbose_name='image Recent')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Recent'
        verbose_name_plural = 'Recents'


class Tournaments(models.Model):
    """Tournaments model"""
    title = models.CharField(max_length=255, verbose_name='Tournament Title')
    image = models.ImageField(upload_to='tournaments_backgrounds/', verbose_name='image Recent')
    start_date = models.DateField(verbose_name='Tournament Begins')
    end_date = models.DateField(verbose_name='Tournament Ends')
    participants_count = models.IntegerField(verbose_name='Participants')
    author = models.CharField(max_length=100, verbose_name='Tournament Author')
    first_place_prize = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='1st Place Prize')
    second_place_prize = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='2nd Place Prize')
    third_place_prize = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='3rd Place Prize')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'


class News(models.Model):
    """News model"""
    body_news = models.CharField(max_length=255, verbose_name='Body news')
    genre = models.ForeignKey(GamesGenre, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='News genre')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return f'{self.body_news}:{self.created_at}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'News'
        verbose_name_plural = 'News'
