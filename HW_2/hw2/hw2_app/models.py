from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.email},{self.phone},{self.address}'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.description},{self.price},{self.quantity}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.products},{self.total_sum}'