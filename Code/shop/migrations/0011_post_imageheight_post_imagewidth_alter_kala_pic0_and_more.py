# Generated by Django 4.0 on 2022-01-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_user_imageheight_user_imagewidth_user_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageheight',
            field=models.PositiveIntegerField(default=401, editable=False),
        ),
        migrations.AddField(
            model_name='post',
            name='imagewidth',
            field=models.PositiveIntegerField(default=401, editable=False),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic0',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/products/20220105-160026', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic1',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20220105 - 160026'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic2',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20220105 - 160026'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic3',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20220105 - 160026'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic4',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20220105 - 160026'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, default='no-image.jpg', height_field='imageheight', null=True, upload_to='static/images/posts/20220105-160026', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/profile/20220105-160026', width_field='imagewidth'),
        ),
    ]