# Generated by Django 4.0.3 on 2022-05-20 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0021_remove_emp_medical_emp_id_delete_stu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('reg_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
