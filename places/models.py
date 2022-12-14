from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Название',
                             max_length=200,
                             unique=True)
    description_short = models.TextField(
        verbose_name='Краткое описание',
        blank=True)
    description_long = HTMLField(
        verbose_name='Длинное описание',
        blank=True)
    latitude = models.FloatField(
        verbose_name='Широта')
    longitude = models.FloatField(
        verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Место'
        verbose_name_plural = "Места"


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images')
    order = models.PositiveIntegerField(
        verbose_name='Позиция',
        default=0,
    )

    def __str__(self):
        return f'{self.order} {self.place}'

    class Meta(object):
        ordering = ['order']
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
