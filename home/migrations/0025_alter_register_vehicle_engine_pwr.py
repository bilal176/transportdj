# Generated by Django 4.0.3 on 2022-05-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_register_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_vehicle',
            name='engine_pwr',
            field=models.CharField(max_length=30),
        ),
    ]
