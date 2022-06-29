from django.db import models

from ..auto_parks.models import AutoParksModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoParksModel, models.CASCADE, 'cars')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
