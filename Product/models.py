from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, quantity: {self.quantity}'
