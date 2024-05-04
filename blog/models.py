from django.conf import settings
from django.db import models
from pytils.translit import slugify

NULLABLE = {"null": True, "blank": True}


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/image/article/', verbose_name='превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    count_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              **NULLABLE, verbose_name='Пользователь')

    def __str__(self):
        return f"{self.title} | {self.is_published} | {self.count_views}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, kwargs)

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
