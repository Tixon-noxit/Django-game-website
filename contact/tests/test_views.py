from django.test import TestCase
from django.urls import reverse
from django.contrib import messages
from unittest.mock import patch
from contact.forms import ContactForm
from contact.models import Contact


class ContactViewTests(TestCase):

    def setUp(self):
        self.url = reverse('contact')
        self.valid_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content.',
        }

        self.contact = Contact.objects.create(
            about_us="Odio ultrices ut. Etiam ac erat ut enim maximus accumsan vel ac nisl. "
                     "Duis feug iat bibendum orci, non elementum urna. Cras sit amet sapien aliquam.",
            address='1481 Creekside Lane Avila Beach, CA 931',
            e_mail="contact@example.com",
            phone="+53 345 7953 32453"
        )

    def test_contact_view_get(self):
        """Тестирую GET запрос к представлению ContactView."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    @patch('contact.views.send_contact_email')
    def test_contact_view_post_valid(self, mock_send_email):
        """Тестирую POST запрос с валидными данными."""
        response = self.client.post(self.url, data=self.valid_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

        form = response.context['form']
        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")

        self.assertTrue(mock_send_email.called, "send_contact_email was not called")

        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(str(messages_list[0]), 'Your message has been sent!')

    def test_contact_view_post_invalid(self):
        """Тестирую POST запрос с невалидными данными."""
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = ''
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertFalse(response.context['form'].is_valid())
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(str(messages_list[0]), 'There was an error sending your message.')
