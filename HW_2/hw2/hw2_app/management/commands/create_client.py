
from random import randint

from django.utils.datetime_safe import datetime
from hw2_app.models import Client
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create clients'

    def handle(self, *args, **kwargs):
        # client = Client(name='Ivon', email='Ivon@mail.ru', phone='12345', address='Ivon str.', date_registered=datetime.now())
        # client = Client(name='Petr', email='Petr@mail.ru', phone='1234544', address='Petr str.',date_registered=datetime.now())
        for client in Client.objects.all():
            for i in range(randint(1, 10)):
                client = Client(
                                name=f'name_{i}',
                                email=f'email_{i}@mail.ru',
                                phone=f'phone{i}',
                                address=f'address{i}',
                                date_registered=datetime.now()
                                )
            client.save()
            self.stdout.write('clients created')