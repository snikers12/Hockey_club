# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20160403_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='guest_score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
