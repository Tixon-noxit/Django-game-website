from django.test import TestCase
from django.urls import reverse
from django.templatetags.static import static
from review.models import Reviews


class ReviewViewTests(TestCase):
    def setUp(self):
        """Создание объектов отзыва для тестов."""
        self.review1 = Reviews.objects.create(
            title="Great Game",
            text="This game was fantastic!",
            rating=9.5,
            image="path/to/review_image1.jpg"
        )
        self.review2 = Reviews.objects.create(
            title="Average Game",
            text="It was okay, nothing special.",
            rating=5.0,
            image="path/to/review_image2.jpg"
        )

    def test_review_view_status_code(self):
        """Проверка, что представление возвращает статус 200."""
        response = self.client.get(reverse('review'))
        self.assertEqual(response.status_code, 200)

    def test_review_view_template_used(self):
        """Проверка, что используется правильный шаблон."""
        response = self.client.get(reverse('review'))
        self.assertTemplateUsed(response, 'review/review.html')

    def test_review_view_context(self):
        """Проверка контекста, возвращаемого представлением."""
        response = self.client.get(reverse('review'))
        self.assertEqual(response.context['page_title'], 'Game reviews')
        self.assertEqual(response.context['page_description'], 'Lorem ipsum dolor sit amet, '
                                                               'consectetur adipiscing elit.'
                                                               ' Donec malesuada lorem maximus mauris scelerisque, '
                                                               'at rutrum nulla dictum.')
        self.assertEqual(len(response.context['reviews']), 2)
        self.assertIn(self.review1, response.context['reviews'])
        self.assertIn(self.review2, response.context['reviews'])

    def test_review_view_background_image_url(self):
        """Проверка корректности URL фона в контексте."""
        response = self.client.get(reverse('review'))
        self.assertEqual(response.context['background_image_url'], static('img/page-top-bg/3.jpg'))