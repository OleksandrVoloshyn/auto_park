from django.db import models


class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    ram = models.IntegerField()
    monitor = models.CharField(max_length=50)
