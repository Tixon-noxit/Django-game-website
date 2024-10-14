from common.views import send_contact_email
import unittest
from unittest.mock import patch


class SendContactEmailTests(unittest.TestCase):

    @patch('common.views.send_mail')
    def test_send_contact_email(self, mock_send_mail):
        name = "John Doe"
        email = "john.doe@example.com"
        subject = "Test Subject"
        message = "This is a test message."

        send_contact_email(name, email, subject, message)

        mock_send_mail.assert_called_once_with(
            subject="Contact Form: Test Subject",
            message="Message from John Doe <john.doe@example.com>:\n\nThis is a test message.",
            from_email=email,
            recipient_list=['admin@example.com'],
            fail_silently=False,
        )

    @patch('common.views.send_mail')
    def test_send_contact_email_with_empty_message(self, mock_send_mail):
        name = "John Doe"
        email = "john.doe@example.com"
        subject = "Test Subject"
        message = ""

        send_contact_email(name, email, subject, message)

        mock_send_mail.assert_called_once_with(
            subject="Contact Form: Test Subject",
            message="Message from John Doe <john.doe@example.com>:\n\n",
            from_email=email,
            recipient_list=['admin@example.com'],
            fail_silently=False,
        )
