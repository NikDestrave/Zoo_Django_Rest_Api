# Generated by Django 3.1.2 on 2020-11-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooapp', '0004_remove_animal_employee_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='employee_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата закрепления'),
        ),
    ]
