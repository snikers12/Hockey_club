# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20160403_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goaltenderstats',
            name='team',
            field=models.ForeignKey(to='team.Team'),
        ),
    ]
