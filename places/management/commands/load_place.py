from pathlib import Path
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image
from places.models import Place


class Command(BaseCommand):
    help = 'Введите ссылку на .json файл с местами для добавления на сайт'

    def add_arguments(self, parser):
        parser.add_argument('load_place', nargs='+', type=str)

    def handle(self, *args, **options):
        for url in options.get('load_place'):
            response = requests.get(url)
            response.raise_for_status()
            place_details = response.json()

        place, _ = Place.objects.get_or_create(
            title=place_details['title'],
            defaults={
                'description_short': place_details['description_short'],
                'description_long': place_details['description_long'],
                'longitude': place_details['coordinates']['lng'],
                'latitude': place_details['coordinates']['lat']
            }
        )

        for image_url in place_details['imgs']:
            response = requests.get(image_url)
            response.raise_for_status()
            content = ContentFile(response.content)
            image_name = Path(urlparse(image_url).path).name
            new_image = Image(place=place)
            new_image.image.save(image_name, content, save=True)
