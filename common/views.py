from django.core.mail import send_mail


def send_contact_email(name, email, subject, message):
    """Отправка письма из формы обратной связи."""
    send_mail(
        subject=f"Contact Form: {subject}",
        message=f"Message from {name} <{email}>:\n\n{message}",
        from_email=email,
        recipient_list=['admin@example.com'],  # Сменить на нужный email
        fail_silently=False,
    )
