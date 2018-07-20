from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article
from .forms import NewArticleForm
from django.urls import reverse


# Create your views here.

class HomeView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_article'] = Article.objects.last()
        return context

class ArticleView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article.html'
    pk_url_kwarg = 'article_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def write_article(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.save()

            article = Article.objects.create(
                message=form.cleaned_data.get('message'),
                article=article,
                creator=request.user
            )
            return redirect('article_page', pk=article.pk)
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {'form': form})
