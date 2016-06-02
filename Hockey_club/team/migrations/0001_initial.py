# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('years', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('founded', models.DateField()),
                ('arena_capacity', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamSeasonStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_played', models.PositiveSmallIntegerField(default=0)),
                ('wins', models.PositiveSmallIntegerField(default=0)),
                ('ot', models.PositiveSmallIntegerField(default=0)),
                ('loses', models.PositiveSmallIntegerField(default=0)),
                ('goals_for', models.PositiveSmallIntegerField(default=0)),
                ('goals_against', models.PositiveSmallIntegerField(default=0)),
                ('points', models.PositiveSmallIntegerField(default=0)),
                ('season', models.ForeignKey(to='team.Season')),
                ('team', models.ForeignKey(to='team.Team')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='teamseasonstats',
            unique_together=set([('team', 'season')]),
        ),
    ]
