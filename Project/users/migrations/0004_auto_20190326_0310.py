# Generated by Django 2.1.7 on 2019-03-25 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190325_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationdata',
            old_name='password',
            new_name='pd',
        ),
        migrations.RenameField(
            model_name='registrationdata',
            old_name='username',
            new_name='user',
        ),
    ]