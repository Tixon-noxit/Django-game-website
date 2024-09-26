from django.test import TestCase
from index.models import Games, Tournaments, GamesGenre, News


class GamesGenreModelTests(TestCase):
    def setUp(self):
        self.genre = GamesGenre.objects.create(name="Action")

    def test_genre_str(self):
        """Проверка строкового представления жанра."""
        self.assertEqual(str(self.genre), "Action")


class GamesModelTests(TestCase):
    def setUp(self):
        self.genre = GamesGenre.objects.create(name="Action")
        self.game = Games.objects.create(
            title="Game Title",
            genre=self.genre,
            text="This is a game description.",
            image="path/to/image.jpg"
        )

    def test_game_str(self):
        """Проверка строкового представления игры."""
        self.assertEqual(str(self.game), "Game Title")

    def test_game_genre(self):
        """Проверка связи с жанром игры."""
        self.assertEqual(self.game.genre.name, "Action")


class TournamentsModelTests(TestCase):
    def setUp(self):
        self.tournament = Tournaments.objects.create(
            title="Summer Tournament",
            image="path/to/tournament.jpg",
            start_date="2024-01-01",
            end_date="2024-01-10",
            participants_count=100,
            author="Author Name",
            first_place_prize=1000.00,
            second_place_prize=500.00,
            third_place_prize=250.00
        )

    def test_tournament_str(self):
        """Проверка строкового представления турнира."""
        self.assertEqual(str(self.tournament), "Summer Tournament")


class NewsModelTests(TestCase):
    def setUp(self):
        self.genre = GamesGenre.objects.create(name="News Genre")
        self.news = News.objects.create(
            body_news="Latest news about gaming.",
            genre=self.genre
        )

    def test_news_str(self):
        """Проверка строкового представления новости."""
        self.assertIn("Latest news about gaming", str(self.news))

    def test_news_genre(self):
        """Проверка связи с жанром новости."""
        self.assertEqual(self.news.genre.name, "News Genre")
