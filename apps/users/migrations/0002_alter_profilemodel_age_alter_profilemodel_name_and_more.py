# Generated by Django 4.0.5 on 2022-07-06 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,50}$', 'only letters min 2 max 100 ch')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^0\\d{9}$', 'Invalid phone number')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='surname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,50}$', 'only letters min 2 max 100 ch')]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\d\\s:])([^\\s]){8,50}$', ['password must contain 1 number (0-9)password must contain 1 uppercase letterspassword must contain 1 lowercase letterspassword must contain 1 non-alpha numeric numberpassword is 8-50 characters with no space'])]),
        ),
    ]