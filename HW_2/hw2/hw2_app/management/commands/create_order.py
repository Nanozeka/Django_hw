
from random import randint
from django.utils.datetime_safe import datetime

from hw2_app.models import Order, Client, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generate test orders'

    def handle(self, *args, **options):

        for i in range(16):

            client = Client.objects.order_by('?').first()
            products = []

            for j in range(randint(1, 5)):
                product = Product.objects.order_by('?').first()
                products.append(product)

            total_sum = randint(500, 5000)

            order = Order.objects.create(
                client=client,
                total_sum=total_sum,
                date_created=datetime.now()
            )

            order.products.set(products)

        self.stdout.write('Generated 16 test orders')