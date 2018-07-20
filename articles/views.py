from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Article
from .forms import NewArticleForm


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
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            a = Article.objects.create(
                subject=form.cleaned_data.get('subject'),
                message=form.cleaned_data.get('message'),
                photo=form.cleaned_data.get('photo'),
                creator=request.user
            )
            a.save()
            return redirect(reverse('new_article_complete'))
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {'form': form})


@login_required
def write_article_complete(request):
    context = {}
    context['last_article'] = Article.objects.last()

    return render(request, 'new_article_complete.html',
                  context=context)


class DeleteSuccessView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'delete_complete.html'
    pk_url_kwarg = 'article_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = Article.objects.filter(id=self.kwargs.get('article_pk')).delete().count(1)

        return context
