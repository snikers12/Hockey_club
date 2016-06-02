# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0011_auto_20160403_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guest_players', models.ManyToManyField(related_name='guest_players', to='team.Player')),
                ('home_players', models.ManyToManyField(related_name='home_players', to='team.Player')),
            ],
        ),
    ]
