# Generated by Django 4.2.2 on 2023-06-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('creator', models.CharField(max_length=250, verbose_name='Имя')),
                ('full_text', models.TextField(verbose_name='Подробнее')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Создатель',
                'verbose_name_plural': 'Создатели',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Подробнее')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('image', models.CharField(max_length=2083)),
            ],
        ),
    ]