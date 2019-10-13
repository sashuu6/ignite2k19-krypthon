# Generated by Django 2.1.7 on 2019-04-01 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_booking_checkin_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='checkout_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]