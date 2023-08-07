from django.db import models
from django.utils import timezone

from core.models import User


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД

    created = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    updated = models.DateTimeField(verbose_name='Дата последнего обновления', default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:  # Когда объект только создается, у него еще нет id
            self.created = timezone.now()  # проставляем дату создания
        self.updated = timezone.now()  # проставляем дату обновления
        return super().save(*args, **kwargs)


class Factory(DatesModelMixin):
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    debt_to_supplier = models.DecimalField(max_digits=10, default=0, decimal_places=2,
                                           verbose_name='Задолженность перед поставщиком')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                             default=None,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class RetailNetwork(DatesModelMixin):
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    number = models.CharField(max_length=10, verbose_name='Номер дома')
    supplier = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='Поставщик (Завод)')
    debt_to_supplier = models.DecimalField(max_digits=10, default=0, decimal_places=2,
                                           verbose_name='Задолженность перед поставщиком')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', default=None)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class IndividualEntrepreneur(DatesModelMixin):
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    number = models.CharField(max_length=10, verbose_name='Номер дома')
    supplier = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE, verbose_name='Поставщик (Розничная сеть)')
    debt_to_supplier = models.DecimalField(max_digits=10, default=0, decimal_places=2,
                                           verbose_name='Задолженность перед поставщиком')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'


class Product(DatesModelMixin):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    category = models.CharField(max_length=100, verbose_name='Категория продукта', default=None, null=True, blank=True)
    model = models.CharField(max_length=100, verbose_name='Модель продукта')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    supplier = models.ForeignKey(IndividualEntrepreneur, on_delete=models.CASCADE, verbose_name='Поставщик (ИП)')
    debt_to_supplier = models.DecimalField(max_digits=10, default=0, decimal_places=2, verbose_name='Задолженность перед поставщиком')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', default=None)
    description = models.TextField(verbose_name='Описание продукта', default=None, null=True)
    image = models.ImageField(upload_to='products/', verbose_name='Изображение продукта', default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0, verbose_name='Рейтинг продукта')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class CartItem(DatesModelMixin):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Название продукта')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
