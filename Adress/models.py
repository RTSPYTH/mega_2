from django.db import models

from Company.models import Company


class Adress(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    home = models.CharField(max_length=50)
    apartment = models.CharField(max_length=50)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'Adress: {self.country, self.city, self.street, self.home, self.apartment}, Company -> {self.company_id}'
