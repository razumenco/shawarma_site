# Generated by Django 4.0.1 on 2022-02-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shawarma_app', '0002_shawarma_standart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.PositiveIntegerField(choices=[(1, 'Мерзко'), (2, 'Невкусно'), (3, 'Нормально'), (4, 'Вкусно'), (5, 'Очень вкусно')]),
        ),
    ]
