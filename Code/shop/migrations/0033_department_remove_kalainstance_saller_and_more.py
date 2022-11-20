# Generated by Django 4.0 on 2022-11-20 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_alter_kala_pic0_alter_kala_pic1_alter_kala_pic2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='kalainstance',
            name='saller',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joind',
        ),
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='imageheight',
        ),
        migrations.RemoveField(
            model_name='user',
            name='imagewidth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='khabarname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.AddField(
            model_name='user',
            name='alergies',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pathologies',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic0',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/products/20221120-212115', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic1',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20221120 - 212115'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic2',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20221120 - 212115'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic3',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20221120 - 212115'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic4',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20221120 - 212115'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, default='no-image.jpg', height_field='imageheight', null=True, upload_to='static/images/posts/20221120-212115', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='salled',
            name='FollowUpCode',
            field=models.CharField(default='7020221120212115', max_length=20),
        ),
        migrations.AlterField(
            model_name='salled',
            name='sent',
            field=models.CharField(choices=[('T', 'Packege sent'), ('F', 'Packege Wait for send'), ('B', 'Back to Store')], default='F', help_text='Is package sent?', max_length=1, verbose_name='Send Status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('image', models.ImageField(default='no-image.jpg', upload_to='static/images/medic/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.department')),
            ],
        ),
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('client_name', models.CharField(blank=True, max_length=50, null=True)),
                ('client_surname', models.CharField(max_length=50)),
                ('client_email', models.EmailField(max_length=50)),
                ('price', models.IntegerField()),
                ('medic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.medic')),
            ],
            options={
                'verbose_name_plural': 'Citation',
            },
        ),
    ]
