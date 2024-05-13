from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='list_article'),
    path('create/', never_cache(ArticleCreateView.as_view()), name='create_article'),
    path('view/<slug:slug>', cache_page(60)(ArticleDetailView.as_view()), name='view_article'),
    path('update/<slug:slug>', never_cache(ArticleUpdateView.as_view()), name='update_article'),
    path('delete/<slug:slug>', never_cache(ArticleDeleteView.as_view()), name='delete_article'),
]