# Generated by Django 4.0.3 on 2022-04-25 15:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=255, verbose_name='Название книги')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('book_image', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Изображение книги')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('release_year', models.IntegerField(default=1900, validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(1900)], verbose_name='Год издания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Рейтинг')),
                ('comments', models.TextField(verbose_name='Комментарии')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'Книги',
                'ordering': ['time_create', 'book_title'],
            },
        ),
    ]
