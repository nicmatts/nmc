from django.forms import ModelForm
from django.utils.text import slugify

from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']

    def save(self):
        instance = super(ArticleForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

        return instance
