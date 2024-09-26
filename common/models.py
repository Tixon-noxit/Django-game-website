from django.db import models


class SiteSettings(models.Model):
    """Настройки сайта"""
    site_name = models.CharField(max_length=255, default="My Website")
    site_description = models.TextField(default="Description of the website")
    site_language = models.CharField(max_length=50, default='ru')
    maintenance_mode = models.BooleanField(default=False)

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance, created = cls.objects.get_or_create(id=1)  # Всегда использую запись с id=1
        return cls._instance

    def save(self, *args, **kwargs):
        self.pk = 1  # Гарантирую, что сохраняется запись с id=1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # Запрещаю удаление записи настроек

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'
