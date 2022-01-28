from django.db import models

from Leader.models import Leader


class Company(models.Model):
    name = models.CharField(max_length=100)
    leader_id = models.ForeignKey(Leader, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, Leader -> {self.leader_id}'
