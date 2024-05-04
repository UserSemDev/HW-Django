from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name="Телефон")
    country = models.CharField(max_length=100, **NULLABLE, verbose_name="Страна")
    avatar = models.ImageField(upload_to='users/avatars/', **NULLABLE, verbose_name="Аватар")

    token = models.CharField(max_length=120, **NULLABLE, verbose_name='Токен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"
