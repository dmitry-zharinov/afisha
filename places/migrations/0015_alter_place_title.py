# Generated by Django 4.1 on 2022-08-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_remove_place_placeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
    ]