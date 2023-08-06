from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Абстрактный базовый класс, Требуется имя пользователя и пароль.
    Другие поля являются необязательными."""
    username = models.CharField(max_length=255, unique=True)
    is_active_employee = models.BooleanField(default=True)
    pass

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'