# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20160403_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldplayerstats',
            name='team',
            field=models.ForeignKey(default=0, to='team.Team'),
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_time',
            field=models.TimeField(default=b'00:00'),
        ),
        migrations.AddField(
            model_name='goaltenderstats',
            name='team',
            field=models.ForeignKey(default=0, to='team.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='fieldplayerstats',
            unique_together=set([('player', 'season', 'team')]),
        ),
        migrations.AlterUniqueTogether(
            name='goaltenderstats',
            unique_together=set([('player', 'season', 'team')]),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('number', 'team')]),
        ),
    ]
