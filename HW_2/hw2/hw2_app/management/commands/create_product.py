
from random import randint

from django.utils.datetime_safe import datetime
from hw2_app.models import Product
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **kwargs):
        product = Product(name='jacket', description='cool jacket', price='12345', quantity='1 ', date_added=datetime.now())

        for product in Product.objects.all():
            for i in range(randint(1, 10)):
                product = Product(
                                name=f'name_{i}',
                                description=f'bla-bla{i}',
                                price=f'{i}',
                                quantity=f'{i}',
                                date_added=datetime.now()
                                )
        product.save()
        self.stdout.write('product created')