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