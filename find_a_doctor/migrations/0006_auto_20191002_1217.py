# Generated by Django 2.2.5 on 2019-10-02 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_doctor', '0005_auto_20191002_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='booked',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
    ]
