from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'is_published', 'count_views', 'created_at',)
    list_filter = ('is_published',)
    search_fields = ('title',)
