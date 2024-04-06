from django.db import models


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
    image = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

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
