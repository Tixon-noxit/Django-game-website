from django.db import models


class Contact(models.Model):
    """Contacts model"""
    about_us = models.TextField(default="Odio ultrices ut. Etiam ac erat ut enim maximus accumsan vel ac nisl. "
                                        "Duis feug iat bibendum orci, non elementum urna. Cras sit amet sapien aliquam.")
    address = models.CharField(max_length=255, verbose_name='address')
    phone = models.CharField(max_length=15, verbose_name='phone')
    e_mail = models.EmailField(verbose_name='email')

    _instance = None

    def __str__(self):
        return 'Contacts'

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance, created = cls.objects.get_or_create(id=1)  # Всегда используем запись с id=1
        return cls._instance

    def save(self, *args, **kwargs):
        self.pk = 1  # Гарантируем, что сохраняется запись с id=1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # Запрет на удаление записи настроек

    class Meta:
        verbose_name = 'Site Contact'
        verbose_name_plural = 'Site Contacts'
