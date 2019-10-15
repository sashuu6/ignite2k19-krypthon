# Generated by Django 2.1.7 on 2019-10-13 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20191013_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='active_status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 9, 14, 43, 74646)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 9, 14, 43, 74646)),
        ),
    ]