# Generated by Django 2.2.2 on 2019-06-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cam_drum_site', '0004_auto_20190628_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]