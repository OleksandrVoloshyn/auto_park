from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    first_name = None
    some_field = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)
