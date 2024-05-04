from django.conf import settings
from django.db import models

from blog.models import NULLABLE


class Category(models.Model):
    """Категория товара"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        """Строковое отображение категории"""
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """Информация о продукте"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/image/product/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              **NULLABLE, verbose_name='Пользователь')

    def __str__(self):
        """Строковое отображение продукта"""
        return f"{self.name} {self.category} {self.price}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    """Контактная информация"""
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    ein = models.CharField(max_length=12, verbose_name="ИНН")

    def __str__(self):
        """Строковое представление контактов"""
        return f"{self.country} | {self.city} | {self.address} | {self.ein}"

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"


class Feedback(models.Model):
    """Обратная связь"""
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=15, verbose_name='Номер')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        """Строковое представление сообщения feedback"""
        return f"{self.name} | {self.phone} | {self.message[0:50]}..."

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Version(models.Model):
    """Версия продукта"""
    winter = "WNR"
    spring = "SRG"
    summer = "SMR"
    autumn = "ATN"
    season_choices = {
        winter: 'Зима',
        spring: 'Весна',
        summer: 'Лето',
        autumn: 'Осень'
    }

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version', verbose_name="Продукт")
    season = models.CharField(max_length=3, choices=season_choices, default=summer, verbose_name="Сезон")
    description = models.TextField(max_length=250, verbose_name="Описание сезона")
    is_active = models.BooleanField(default=True, verbose_name="Активный сезон")

    def __str__(self):
        return f"{self.product}, {self.season}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
