from review.models import Reviews
from django.templatetags.static import static
from django.utils import timezone
from django.urls import reverse
from django.test import TestCase
from index.models import Games, Tournaments, GamesGenre, News


class HomeViewTests(TestCase):

    def setUp(self):
        self.genre = GamesGenre.objects.create(name='New')
        self.game = Games.objects.create(title='Test Game', genre=self.genre, text='Test text',
                                         image=static('img/review/1.jpg'), )

        self.tournament = Tournaments.objects.create(
            title='Test title',
            image=static('img/review/1.jpg'),
            start_date=timezone.now(),
            end_date=timezone.now(),
            participants_count=50,
            author='Admin',
            first_place_prize=5000,
            second_place_prize=3000,
            third_place_prize=1000)

        self.review = Reviews.objects.create(
            title='Great game!',
            text='Great game!',
            rating=5.4,
            image=static('img/review/1.jpg'),
        )

    def test_home_view_status_code(self):
        """Проверка, что home_view возвращает статус 200."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        """Проверка, что home_view использует правильный шаблон."""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index/index.html')

    def test_home_view_context_data(self):
        """Проверка, что home_view передает правильные данные в контексте."""
        response = self.client.get(reverse('index'))
        self.assertIn('recent_games', response.context)
        self.assertIn('tournament_games', response.context)
        self.assertIn('reviews', response.context)

        self.assertEqual(response.context['recent_games'].count(), 1)
        self.assertEqual(response.context['tournament_games'].count(), 1)
        self.assertEqual(response.context['reviews'].count(), 1)

        self.assertEqual(response.context['recent_games'].first(), self.game)
        self.assertEqual(response.context['tournament_games'].first(), self.tournament)
        self.assertEqual(response.context['reviews'].first(), self.review)