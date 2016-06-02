# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album_name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=gallery.models.get_photo_image_path, blank=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(to='gallery.Album')),
            ],
        ),
    ]
