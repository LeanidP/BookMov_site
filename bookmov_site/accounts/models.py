
from django.db import models


class Accounts(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name="Имя пользователя")
    password = models.CharField(max_length=255, verbose_name="Пароль")
    password2 = models.CharField(max_length=255, verbose_name="Повторение пароля")
    email = models.EmailField(max_length=70, unique=True, verbose_name="Электронная почта")
    user_photo = models.ImageField(upload_to="avatar/%Y/%m/%d/", verbose_name="Фото пользователя")
    area_of_residence = models.CharField(max_length=50, verbose_name="Район проживания")
    comments = models.TextField(blank=False, verbose_name="Комментарии")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ['registration_date', 'username']
