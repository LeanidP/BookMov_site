from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Books(models.Model):
    book_title = models.CharField(max_length=255, verbose_name="Название книги")
    book_image = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name="Изображение книги")
    author = models.CharField(max_length=50, verbose_name="Автор")
    release_year = models.IntegerField(default=1900,
                                       validators=[MaxValueValidator(2022), MinValueValidator(1900)],
                                       verbose_name="Год издания")
    description = models.TextField(blank=False, verbose_name="Описание")
    rating = models.IntegerField(default=1,
                                 validators=[MaxValueValidator(10), MinValueValidator(1)],
                                 verbose_name="Рейтинг")
    comments = models.TextField(blank=False, verbose_name="Комментарии")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    user_author = models.CharField(max_length=255, null=True, verbose_name="Владелец книги")
    info_author = models.CharField(max_length=255, null=True, verbose_name='Контакты владельца')


    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ['time_create', 'book_title']



