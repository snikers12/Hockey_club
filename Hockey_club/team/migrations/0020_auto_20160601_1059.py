# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-01 07:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0019_auto_20160528_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 6, 1, 10, 59, 20, 290000)),
        ),
    ]
