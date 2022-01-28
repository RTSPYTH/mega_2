from django.db import models

from Leader.models import Leader


class BankAccount(models.Model):
    payment = models.PositiveIntegerField()
    owner_id = models.ForeignKey(Leader, on_delete=models.CASCADE)

    def __str__(self):
        return f'Payment = {self.payment}, Owner -> {self.owner_id}'
