import csv

from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for device in phones:
            # TODO: Добавьте сохранение модели
            phone = Phone(id = device.get('id'),
                          name = device.get('name'),
                          image = device.get('image'),
                          price = device.get('price'),
                          release_date = device.get('release_date'),
                          lte_exists = device.get('lte_exists'),
                          slug=slugify(device.get('name'))
                          )
            phone.save()
