# Generated by Django 4.0.3 on 2022-04-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_stu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
