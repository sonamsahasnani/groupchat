# Generated by Django 3.2.20 on 2023-08-05 18:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0007_alter_group_created_at'),
        ('group_messages', '0004_alter_message_messaged_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='group.group'),
        ),
        migrations.AlterField(
            model_name='message',
            name='messaged_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 5, 18, 6, 4, 601982)),
        ),
    ]
