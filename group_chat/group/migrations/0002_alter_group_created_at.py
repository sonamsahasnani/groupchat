# Generated by Django 3.2.20 on 2023-07-23 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 8, 38, 37, 723857)),
        ),
    ]
