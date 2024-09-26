from django.test import TestCase
from django.utils import timezone
from forum.models import ForumPost
from django.templatetags.static import static


class ForumPostModelTest(TestCase):

    def setUp(self):
        self.post = ForumPost.objects.create(
            author='Test Author',
            content='Test content',
            avatar=static('img/authors/1.jpg'),
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

    def test_forum_post_creation(self):
        """Проверка, что пост создан с правильными данными."""
        post = ForumPost.objects.get(id=self.post.id)
        self.assertEqual(post.author, 'Test Author')
        self.assertEqual(post.content, 'Test content')
        self.assertTrue(post.avatar.name.endswith('img/authors/1.jpg'))
        self.assertIsNotNone(post.created_at)
        self.assertIsNotNone(post.updated_at)

    def test_forum_post_str_method(self):
        """Проверка строкового представления ForumPost."""
        post = ForumPost.objects.get(id=self.post.id)
        self.assertEqual(str(post), f"{post.author} - {post.content}")

    def test_forum_post_ordering(self):
        """Проверка, что посты отсортированы по дате создания (по убыванию)."""
        post1 = ForumPost.objects.create(author='Author 1', content='Content 1', created_at=timezone.now())
        post2 = ForumPost.objects.create(author='Author 2', content='Content 2', created_at=timezone.now())
        posts = ForumPost.objects.all()
        self.assertEqual(posts[0], post2)
        self.assertEqual(posts[1], post1)