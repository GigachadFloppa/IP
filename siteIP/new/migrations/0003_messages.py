# Generated by Django 3.2.5 on 2021-07-10 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_alter_articles_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('city', models.CharField(max_length=250, verbose_name='City')),
                ('email', models.CharField(max_length=250, verbose_name='Email')),
                ('message', models.CharField(max_length=250, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Обр.связь',
                'verbose_name_plural': 'Обр.связь',
            },
        ),
    ]
