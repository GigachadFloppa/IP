# Generated by Django 3.2.5 on 2021-07-03 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='ФИО')),
                ('role', models.CharField(max_length=50, verbose_name='Должность')),
                ('skills', models.CharField(max_length=250, verbose_name='Навыки')),
                ('full_text', models.TextField(verbose_name='Основной текст')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
