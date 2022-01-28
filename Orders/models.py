from django.db import models

from Company.models import Company
from Product.models import Product


class Order(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_quantity = models.PositiveIntegerField()
    sale_date = models.DateField()

    def __str__(self):
        return f'Company -> {self.company_id}, Product -> {self.product_id}, quantity: {self.sale_quantity}, ' \
               f'date: {self.sale_date}'
