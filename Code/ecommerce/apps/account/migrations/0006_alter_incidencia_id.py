# Generated by Django 3.2 on 2022-12-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20221211_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidencia',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
