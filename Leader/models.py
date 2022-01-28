from django.db import models


class Leader(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
