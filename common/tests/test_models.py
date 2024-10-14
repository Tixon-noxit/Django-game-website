from django.test import TestCase
from common.models import SiteSettings


class SiteSettingsTestCase(TestCase):
    def setUp(self):
        self.settings = SiteSettings.objects.create(
            site_name="Test Website",
            site_description="Test Description",
            site_language="en",
            maintenance_mode=False
        )

    def test_get_instance(self):
        instance = SiteSettings.get_instance()
        self.assertEqual(instance.site_name, "Test Website")
        self.assertEqual(instance.site_description, "Test Description")
        self.assertEqual(instance.site_language, "en")
        self.assertFalse(instance.maintenance_mode)

    def test_singleton_behavior(self):
        instance1 = SiteSettings.get_instance()
        instance2 = SiteSettings.get_instance()
        self.assertIs(instance1, instance2)

    def test_save_overwrites_instance(self):
        instance = SiteSettings.get_instance()
        instance.site_name = "Updated Website"
        instance.save()

        updated_instance = SiteSettings.get_instance()
        self.assertEqual(updated_instance.site_name, "Updated Website")

    def test_delete_is_forbidden(self):
        instance = SiteSettings.get_instance()
        instance_id = instance.id
        instance.delete()

        remaining_instance = SiteSettings.get_instance()
        self.assertEqual(remaining_instance.id, instance_id)
        self.assertEqual(remaining_instance.site_name, "Test Website")

    def test_initial_values(self):
        SiteSettings.objects.all().delete()
        instance = SiteSettings.get_instance()

        self.assertEqual(instance.site_name, "Test Website")
        self.assertEqual(instance.site_description, "Test Description")
        self.assertEqual(instance.site_language, "en")
        self.assertFalse(instance.maintenance_mode)
