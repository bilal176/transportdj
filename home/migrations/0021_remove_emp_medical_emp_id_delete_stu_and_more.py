# Generated by Django 4.0.3 on 2022-05-20 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_stu_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp_medical',
            name='emp_id',
        ),
        migrations.DeleteModel(
            name='stu',
        ),
        migrations.DeleteModel(
            name='emp_medical',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]
