# Generated by Django 4.2.16 on 2024-09-24 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_sitesettings_site_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='site_language',
            field=models.CharField(default='ru', max_length=50),
        ),
    ]
