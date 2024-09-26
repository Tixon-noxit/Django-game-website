from django.test import TestCase
from contact.forms import ContactForm


class ContactFormTest(TestCase):

    def test_contact_form_valid_data(self):
        """Проверка валидации формы с корректными данными."""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test subject',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_missing_data(self):
        """Проверка, что форма невалидна при отсутствии обязательных данных."""
        form_data = {
            'name': 'John Doe',
            'email': '',
            'subject': 'Test subject',
            'message': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertIn('message', form.errors)

    def test_contact_form_invalid_email(self):
        """Проверка, что форма невалидна с некорректным email."""
        form_data = {
            'name': 'John Doe',
            'email': 'invalid-email',
            'subject': 'Test subject',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
