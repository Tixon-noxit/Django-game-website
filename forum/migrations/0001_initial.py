# Generated by Django 4.2.16 on 2024-09-25 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='/static/img/authors/8.jpg', upload_to='comment_images/', verbose_name='image ForumPost')),
                ('author', models.CharField(max_length=255, verbose_name='author ForumPost')),
                ('content', models.TextField(verbose_name='text ForumPost')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'ForumPost',
                'verbose_name_plural': 'ForumPosts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ForumPostAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/', verbose_name='Attachment File')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded At')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='forum.forumpost', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Post Attachment',
                'verbose_name_plural': 'Post Attachments',
            },
        ),
    ]
