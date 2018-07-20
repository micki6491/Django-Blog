from django.views.generic import ListView, DetailView
from .models import Article
from tinymce.models import HTMLField


# Create your views here.

class HomeView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'home.html'
    content = HTMLField()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_article'] = Article.objects.last()
        return context


class ArticleView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article.html'
    pk_url_kwarg = 'article_pk'
