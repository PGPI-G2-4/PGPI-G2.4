# Generated by Django 4.0 on 2022-03-06 16:43

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_alter_user_managers_alter_kala_pic0_alter_kala_pic1_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic0',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/products/20220306-164349', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic1',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20220306 - 164349'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic2',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20220306 - 164349'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic3',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20220306 - 164349'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic4',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20220306 - 164349'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, default='no-image.jpg', height_field='imageheight', null=True, upload_to='static/images/posts/20220306-164349', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='salled',
            name='FollowUpCode',
            field=models.CharField(default='9920220306164349', max_length=20),
        ),
        migrations.AlterField(
            model_name='salled',
            name='sent',
            field=models.CharField(choices=[('F', 'Packege Wait for send'), ('B', 'Back to Store'), ('T', 'Packege sent')], default='F', help_text='Is package sent?', max_length=1, verbose_name='Send Status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/profile/20220306-164349', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=30, null=True, verbose_name='email address'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
