from django.core.urlresolvers import reverse_lazy

from .models import Article

from vanilla import CreateView, DeleteView, ListView, UpdateView, DetailView


class ListArticles(ListView):
    model = Article


class ArticleDetail(DetailView):
    model = Article
    lookup_field = 'slug'
