from django.shortcuts import render
from django.templatetags.static import static
from . import forms
from . import models
from common.views import send_contact_email
from django.contrib import messages
from django.views.generic import View


class ContactView(View):
    form_class = forms.ContactForm
    template_name = 'contact/contact.html'

    def get(self, request):
        form = self.form_class()
        return self.render_page(form)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.process_form(form)
            messages.success(request, 'Your message has been sent!')
        else:
            messages.error(request, 'There was an error sending your message.')

        return self.render_page(form)

    def process_form(self, form):
        """Обработка и отправка формы."""
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        send_contact_email(name, email, subject, message)

    def get_context(self, form):
        """Создание контекста для рендеринга страницы."""
        return {
            'page_title': 'Contact us',
            'page_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada '
                                'lorem maximus mauris scelerisque, at rutrum nulla dictum.',
            'background_image_url': static('img/page-top-bg/5.jpg'),
            'contacts': models.Contact.objects.get(id=1) or 0,
            'form': form,
        }

    def render_page(self, form):
        """Рендер страницы с контекстом."""
        context = self.get_context(form)
        return render(self.request, self.template_name, context)

