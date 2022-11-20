# Generated by Django 3.2.9 on 2021-12-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20211211_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kala',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, default='no-image.jpg', height_field='imageheight', null=True, upload_to='static/images/logos/', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic0',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/products/20211212-132957', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic1',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20211212 - 132957'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic2',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20211212 - 132957'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic3',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20211212 - 132957'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic4',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20211212 - 132957'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/posts/20211212-132957'),
        ),
    ]
