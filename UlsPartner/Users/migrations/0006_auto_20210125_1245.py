# Generated by Django 3.0 on 2021-01-25 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_profile_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Phone_Number',
            field=models.CharField(default=' ', max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')]),
        ),
    ]