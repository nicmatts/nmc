from django.conf.urls import patterns, include, url
from .models import Article
from .views import ArticleDetail

urlpatterns = patterns('',
    #url(r'^$', ListNotes.as_view(), name='list_notes'),
    #url(r'^create/$', CreateNote.as_view(), name='create_note'),
    url(r'^(?P<slug>[\w-]+)/$', ArticleDetail.as_view(), name='article_detail'),
)
