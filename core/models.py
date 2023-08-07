from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from .managers import UserManager, UserRoles


class User(AbstractUser, PermissionsMixin):
    """Абстрактный базовый класс, Требуется имя пользователя и пароль.
    Другие поля являются необязательными."""
    username = models.CharField(max_length=255, unique=True)
    is_active_employee = models.BooleanField(default=True)
    role = models.CharField(max_length=3, choices=UserRoles.choices, default=UserRoles.USER)
    # objects = UserManager()


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'