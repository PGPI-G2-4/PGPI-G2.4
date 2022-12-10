# Generated by Django 3.2 on 2022-12-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryoptions',
            name='delivery_method',
            field=models.CharField(choices=[('MAIL', 'We will send it to you by mail'), ('REGISTER YOUR DATA', 'Keep track of all your appointments by providing some information'), ('SMS', 'We will send you an SMS with a link to your appointment')], help_text='Required', max_length=255, verbose_name='delivery_method'),
        ),
    ]
