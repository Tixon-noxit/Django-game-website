from django.test import TestCase
from django.core.exceptions import ValidationError
from review.models import Reviews


class ReviewsModelTests(TestCase):
    def setUp(self):
        """Создание объекта отзыва для тестов."""
        self.review = Reviews.objects.create(
            title="Great Game",
            text="This game was fantastic!",
            rating=9.5,
            image="path/to/review_image.jpg"
        )

    def test_review_str(self):
        """Проверка строкового представления отзыва."""
        self.assertEqual(str(self.review), "Great Game")

    def test_rating_within_valid_range(self):
        """Проверка, что рейтинг в пределах допустимого диапазона."""
        self.review.rating = 10.0
        try:
            self.review.full_clean()
        except ValidationError:
            self.fail("ValidationError raised when rating is within valid range")

    def test_rating_below_minimum(self):
        """Проверка, что рейтинг ниже минимального значения вызывает ValidationError."""
        self.review.rating = -1.0
        with self.assertRaises(ValidationError):
            self.review.full_clean()

    def test_rating_above_maximum(self):
        """Проверка, что рейтинг выше максимального значения вызывает ValidationError."""
        self.review.rating = 11.0
        with self.assertRaises(ValidationError):
            self.review.full_clean()

    def test_review_creation(self):
        """Проверка создания объекта отзыва."""
        self.assertIsInstance(self.review, Reviews)
        self.assertEqual(self.review.title, "Great Game")
        self.assertEqual(self.review.text, "This game was fantastic!")
        self.assertEqual(self.review.rating, 9.5)


