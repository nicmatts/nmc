from django.conf.urls import patterns, include, url
from .models import Article
from .views import ArticleDetail, ListArticles

urlpatterns = patterns('',
    url(r'^$', ListArticles.as_view(), name='list_articles'),
    #url(r'^create/$', CreateNote.as_view(), name='create_note'),
    url(r'^(?P<slug>[\w-]+)/$', ArticleDetail.as_view(), name='article_detail'),
)
