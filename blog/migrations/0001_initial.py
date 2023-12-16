# Generated by Django 4.2.7 on 2023-11-23 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Содержание')),
                ('image', models.ImageField(upload_to='post_image/', verbose_name='Картинка поста')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 11, 23, 13, 29, 58, 274942, tzinfo=datetime.timezone.utc), verbose_name='Дата создания поста')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]