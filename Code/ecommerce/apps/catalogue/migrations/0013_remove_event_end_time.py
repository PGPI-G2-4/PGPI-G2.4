# Generated by Django 3.2 on 2022-12-08 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_auto_20221207_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
    ]
