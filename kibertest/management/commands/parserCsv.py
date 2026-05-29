import csv

from django.core.management import BaseCommand

from kibertest.models import Card


class Command(BaseCommand):
    def handle(self, *args, **options):
        Card.objects.all().delete()
        with open("Cards.csv",newline="") as csvFile:
            csvFileReader = csv.reader(csvFile,delimiter=';')
            for row in csvFileReader:
                Card.objects.create(number=row[0],nameBank=row[1],system=row[2])

