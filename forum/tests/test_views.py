from django.test import TestCase
from django.urls import reverse
from django.templatetags.static import static
from forum.models import ForumPost



class ForumListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_posts = 10
        for post_num in range(number_of_posts):
            ForumPost.objects.create(
                avatar=static('img/authors/1.jpg'),
                author='James Smith',
                content='Test content',
            )

    def test_view_url_exists_at_desired_location(self):
        """Проверка, что URL доступен."""
        response = self.client.get('/forum/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Проверка, что используется правильный шаблон."""
        response = self.client.get(reverse('forum'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/forum.html')

    def test_view_context_data(self):
        """Проверка контекстных данных."""
        response = self.client.get(reverse('forum'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('page_title', response.context)
        self.assertIn('page_description', response.context)
        self.assertEqual(response.context['page_title'], 'Our Community')
        self.assertEqual(response.context['page_description'], 'Lorem ipsum dolor sit amet, consectetur '
                                                               'adipiscing elit. Donec malesuada lorem maximus '
                                                               'mauris scelerisque, at rutrum nulla dictum.')
        self.assertEqual(response.context['background_image_url'], static('img/page-top-bg/4.jpg'))

    def test_pagination_is_seven(self):
        """Проверка, что на странице отображается 7 постов."""
        response = self.client.get(reverse('forum'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['posts']), 7)

    def test_lists_all_posts(self):
        """Проверка второй страницы пагинации и общего количества постов."""
        response = self.client.get(reverse('forum') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 3)


