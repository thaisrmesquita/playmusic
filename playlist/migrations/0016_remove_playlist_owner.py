# Generated by Django 2.0.6 on 2018-08-08 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0015_auto_20180807_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='owner',
        ),
    ]
