import os

from django.db import models
from user.models import UserModel


# Create your models here.

def user_directory_path(instance, filename):
    return os.path.join(f'{instance.user.username}', filename)


class CarModel(models.Model):
    class Meta:
        db_table = 'car'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    photo = models.ImageField(upload_to=user_directory_path)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
