from django.test import TestCase
from contact.models import Contact


class ContactModelTest(TestCase):

    def setUp(self):
        self.contact_data = {
            'about_us': "Sample about us text.",
            'address': "123 Test St.",
            'phone': "1234567890",
            'e_mail': "test@example.com"
        }

    def test_create_contact(self):
        """Проверка создания и сохранения контакта с id=1."""
        contact = Contact(**self.contact_data)
        contact.save()

        saved_contact = Contact.objects.get(id=1)
        self.assertEqual(saved_contact.address, "123 Test St.")
        self.assertEqual(saved_contact.phone, "1234567890")
        self.assertEqual(saved_contact.e_mail, "test@example.com")

    def test_get_instance_returns_single_instance(self):
        """Проверка, что метод get_instance всегда возвращает экземпляр с id=1."""
        contact1 = Contact.get_instance()
        contact2 = Contact.get_instance()

        self.assertEqual(contact1, contact2)
        self.assertEqual(contact1.id, 1)

    def test_save_forces_id_1(self):
        """Проверка, что метод save всегда устанавливает id=1."""
        contact = Contact(**self.contact_data)
        contact.save()

        contact.pk = 2
        contact.save()

        saved_contact = Contact.objects.get(id=1)
        self.assertEqual(saved_contact.pk, 1)

    def test_default_values(self):
        """Проверка дефолтных значений в поле about_us."""
        contact = Contact.get_instance()
        self.assertEqual(contact.about_us, "Odio ultrices ut. Etiam ac erat ut enim maximus accumsan vel ac nisl. "
                                           "Duis feug iat bibendum orci, non elementum urna. "
                                           "Cras sit amet sapien aliquam.")
