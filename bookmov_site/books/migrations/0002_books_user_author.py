# Generated by Django 4.0.3 on 2022-04-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='user_author',
            field=models.CharField(max_length=255, null=True, verbose_name='Владелец книги'),
        ),
    ]
