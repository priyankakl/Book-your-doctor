# Generated by Django 2.2.5 on 2019-10-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('experience', models.IntegerField()),
                ('fee', models.IntegerField()),
                ('Available', models.CharField(max_length=200)),
            ],
        ),
    ]
