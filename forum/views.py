from django.templatetags.static import static
from django.views.generic import ListView
from . import models


class ForumListView(ListView):
    """Forum view"""
    model = models.ForumPost
    template_name = 'forum/forum.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Our Community'
        context[
            'page_description'] = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada ' \
                                  'lorem maximus mauris scelerisque, at rutrum nulla dictum.'
        context['background_image_url'] = static('img/page-top-bg/4.jpg')
        return context
