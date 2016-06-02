# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0012_matchstats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchstats',
            name='guest_players',
        ),
        migrations.RemoveField(
            model_name='matchstats',
            name='home_players',
        ),
        migrations.DeleteModel(
            name='MatchStats',
        ),
    ]
