# Generated by Django 3.0 on 2021-01-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20210121_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='FullName',
            field=models.CharField(default='', max_length=79),
        ),
    ]