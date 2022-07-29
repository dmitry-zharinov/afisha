# Generated by Django 3.2.14 on 2022-07-29 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description_short', models.CharField(max_length=200, verbose_name='Краткое описание')),
                ('description_long', models.TextField(blank=True, verbose_name='Длинное описание')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
            ],
        ),
    ]
