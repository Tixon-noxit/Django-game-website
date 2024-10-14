from django.templatetags.static import static
from index.models import Games
from django.views.generic import ListView


class BlogListView(ListView):
    """Blog view"""
    model = Games
    template_name = 'blog/blog.html'
    context_object_name = 'articles'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Video Gallery'
        context[
            'page_description'] = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada ' \
                                  'lorem maximus mauris scelerisque, at rutrum nulla dictum.'
        context['background_image_url'] = static('img/page-top-bg/1.jpg')
        return context
