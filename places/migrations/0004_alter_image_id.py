# Generated by Django 3.2.14 on 2022-08-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]