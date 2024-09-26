from django.test import TestCase
from django.urls import reverse
from index.models import Games
from django.templatetags.static import static


class BlogListViewTests(TestCase):
    def setUp(self):
        for i in range(15):
            Games.objects.create(title=f'Game {i}', text='Lorem ipsum dolor sit amet, '
                                                         'consectetur adipisc ing ipsum '
                                                         'dolor sit ame.',
                                 image=static('img/review/1.jpg'))

    def test_blog_list_view_status_code(self):
        """Тестируем статус код представления"""
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_blog_list_view_template_used(self):
        """Проверяем, что используется правильный шаблон"""
        response = self.client.get(reverse('blog'))
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_blog_list_view_context(self):
        """Проверяем контекст представления"""
        response = self.client.get(reverse('blog'))
        self.assertIn('page_title', response.context)
        self.assertEqual(response.context['page_title'], 'Video Gallery')

        self.assertIn('page_description', response.context)
        self.assertEqual(response.context['page_description'],
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                         'Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum.')

        self.assertIn('background_image_url', response.context)
        self.assertEqual(response.context['background_image_url'], static('img/page-top-bg/1.jpg'))

    def test_blog_list_view_paginate_by(self):
        """Проверяем пагинацию"""
        response = self.client.get(reverse('blog'))
        self.assertEqual(len(response.context['articles']), 8)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])

    def test_blog_list_view_pagination_second_page(self):
        """Проверяем, что на второй странице отображается правильное количество статей"""
        response = self.client.get(reverse('blog') + '?page=2')
        self.assertEqual(len(response.context['articles']),
                         7)
