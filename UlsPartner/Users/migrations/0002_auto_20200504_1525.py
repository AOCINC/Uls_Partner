# Generated by Django 3.0 on 2020-05-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='CIN_Number',
            field=models.CharField(blank=True, max_length=21),
        ),
        migrations.AlterField(
            model_name='profile',
            name='GST_Number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Pan_Number',
            field=models.CharField(blank=True, default='PAN Number', max_length=10),
        ),
    ]