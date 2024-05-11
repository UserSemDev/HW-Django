from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import ArticleForm
from blog.models import Article
from config.settings import EMAIL_HOST_USER, EMAIL_HOST_TO_USER


class ArticleListView(ListView):
    model = Article
    extra_context = {
        "title": "Cтатьи"
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'blog.view_article'
    model = Article
    extra_context = {
        "title": "Статья"
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        if self.object.count_views == 100:
            send_mail(
                subject='Оповещение о количестве просмотров статьи.',
                message=f'Статья [{self.object.title}] достигла {self.object.count_views} просмотров!',
                from_email=EMAIL_HOST_USER,
                recipient_list=[EMAIL_HOST_TO_USER],
                fail_silently=False,
            )

        return self.object


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_article'
    model = Article
    form_class = ArticleForm
    extra_context = {
        "title": "Добавление статьи"
    }

    def get_success_url(self):
        return reverse('blog:view_article', args=[self.object.slug])

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_article'
    model = Article
    form_class = ArticleForm
    extra_context = {
        "title": "Редактирование статьи"
    }

    def get_success_url(self):
        return reverse('blog:view_article', args=[self.object.slug])


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'blog.delete_article'
    model = Article
    extra_context = {
        "title": "Удаление статьи"
    }
    success_url = reverse_lazy('blog:list_article')
