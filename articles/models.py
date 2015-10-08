from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return "%s" % (self.name)


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default="TKTK")
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField()
    # created = models.DateTimeField(auto_now=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)
