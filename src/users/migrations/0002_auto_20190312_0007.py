# Generated by Django 2.1.7 on 2019-03-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='img1.jpg', upload_to='profile_pics'),
        ),
    ]
