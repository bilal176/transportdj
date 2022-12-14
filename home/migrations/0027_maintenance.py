# Generated by Django 4.0.3 on 2022-05-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='maintenance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('driver_id', models.CharField(max_length=100, null=True)),
                ('vid', models.CharField(max_length=100, null=True)),
                ('meachanice_id', models.CharField(max_length=100, null=True)),
                ('problem', models.CharField(max_length=5000, null=True)),
                ('workdone', models.CharField(max_length=5000, null=True)),
                ('ewr', models.BooleanField()),
                ('date1', models.DateTimeField()),
            ],
            options={
                'db_table': 'maintenance',
            },
        ),
    ]
