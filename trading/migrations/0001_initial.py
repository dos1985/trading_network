# Generated by Django 4.0.1 on 2023-08-06 06:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата последнего обновления')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность перед поставщиком')),
            ],
            options={
                'verbose_name': 'Завод',
                'verbose_name_plural': 'Заводы',
            },
        ),
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата последнего обновления')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность перед поставщиком')),
            ],
            options={
                'verbose_name': 'Индивидуальный предприниматель',
                'verbose_name_plural': 'Индивидуальные предприниматели',
            },
        ),
        migrations.CreateModel(
            name='RetailNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата последнего обновления')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность перед поставщиком')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.factory', verbose_name='Поставщик (Завод)')),
            ],
            options={
                'verbose_name': 'Розничная сеть',
                'verbose_name_plural': 'Розничные сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата последнего обновления')),
                ('name', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('model', models.CharField(max_length=100, verbose_name='Модель продукта')),
                ('release_date', models.DateField(verbose_name='Дата выхода продукта на рынок')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность перед поставщиком')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.individualentrepreneur', verbose_name='Поставщик (ИП)')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.AddField(
            model_name='individualentrepreneur',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.retailnetwork', verbose_name='Поставщик (Розничная сеть)'),
        ),
    ]
