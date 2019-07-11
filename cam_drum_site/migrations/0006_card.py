# Generated by Django 2.2.2 on 2019-07-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cam_drum_site', '0005_auto_20190628_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=600)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
