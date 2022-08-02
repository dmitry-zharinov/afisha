from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    description_short = models.CharField(
        verbose_name='Краткое описание',
        max_length=300)
    description_long = models.TextField(
        verbose_name='Длинное описание',
        blank=True)
    latitude = models.FloatField(
        verbose_name='Широта')
    longitude = models.FloatField(
        verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    index_num = models.IntegerField(null=True)
    image = models.ImageField(upload_to='img', null=True)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images')

    def __str__(self):
        return f'{self.index_num} {self.place}'
