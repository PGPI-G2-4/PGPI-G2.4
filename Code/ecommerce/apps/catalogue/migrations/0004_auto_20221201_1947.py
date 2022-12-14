# Generated by Django 3.2 on 2022-12-01 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20221201_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='users_wishlist',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productspecification',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='productspecificationvalue',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productspecificationvalue',
            name='specification',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
