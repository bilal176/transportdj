# Generated by Django 4.0.3 on 2022-05-26 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_city_alter_maintenance_ewr'),
    ]

    operations = [
        migrations.CreateModel(
            name='routte',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=100, unique=True)),
                ('rname', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'routte',
            },
        ),
    ]
