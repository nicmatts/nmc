from django.contrib import admin

from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
