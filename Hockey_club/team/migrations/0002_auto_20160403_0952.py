# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('founded', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FieldPlayerStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('games_played', models.PositiveSmallIntegerField(default=0)),
                ('goals', models.PositiveSmallIntegerField(default=0)),
                ('assists', models.PositiveSmallIntegerField(default=0)),
                ('points', models.PositiveSmallIntegerField(default=0)),
                ('penalty_minutes', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoaltenderStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('games_played', models.PositiveSmallIntegerField(default=0)),
                ('wins', models.PositiveSmallIntegerField(default=0)),
                ('goals_against', models.PositiveSmallIntegerField(default=0)),
                ('null', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('home_score', models.PositiveSmallIntegerField()),
                ('guest_score', models.PositiveSmallIntegerField()),
                ('ot', models.CharField(blank=True, max_length=2, choices=[(b'OT', b'Overtime'), (b'SO', b'Shootout')])),
                ('match_ended', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=2, choices=[(b'LW', b'Left Winger'), (b'C', b'Center'), (b'D', b'Defenceman'), (b'RW', b'Right Winger'), (b'G', b'Goaltender')])),
                ('birthday', models.DateField()),
                ('height', models.PositiveSmallIntegerField()),
                ('weight', models.PositiveSmallIntegerField()),
                ('playing_now', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamStuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50, choices=[(b'GC', b"Goaltender's coach"), (b'HC', b'Head coach'), (b'D', b'Doctor'), (b'C', b'Coach'), (b'P', b'President'), (b'M', b'Masseur'), (b'GM', b'General manager')])),
            ],
        ),
        migrations.RenameField(
            model_name='teamseasonstats',
            old_name='game_played',
            new_name='games_played',
        ),
        migrations.RemoveField(
            model_name='team',
            name='arena_capacity',
        ),
        migrations.AddField(
            model_name='team',
            name='is_alive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='teamstuff',
            name='team',
            field=models.ForeignKey(default=1, to='team.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=1, to='team.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='guest',
            field=models.ForeignKey(related_name='guest', to='team.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home',
            field=models.ForeignKey(related_name='home', to='team.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='season',
            field=models.ForeignKey(default=0, to='team.Season'),
        ),
        migrations.AddField(
            model_name='goaltenderstats',
            name='player',
            field=models.ForeignKey(to='team.Player'),
        ),
        migrations.AddField(
            model_name='goaltenderstats',
            name='season',
            field=models.ForeignKey(to='team.Season'),
        ),
        migrations.AddField(
            model_name='goal',
            name='assist1',
            field=models.ForeignKey(related_name='assist1', blank=True, to='team.Player', null=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='assist2',
            field=models.ForeignKey(related_name='assist2', blank=True, to='team.Player', null=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_scorer',
            field=models.ForeignKey(related_name='goal_scorer', to='team.Player'),
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_scorer_team',
            field=models.ForeignKey(to='team.Team'),
        ),
        migrations.AddField(
            model_name='goal',
            name='match',
            field=models.ForeignKey(to='team.Match'),
        ),
        migrations.AddField(
            model_name='fieldplayerstats',
            name='player',
            field=models.ForeignKey(to='team.Player'),
        ),
        migrations.AddField(
            model_name='fieldplayerstats',
            name='season',
            field=models.ForeignKey(to='team.Season'),
        ),
        migrations.AddField(
            model_name='team',
            name='arena',
            field=models.ForeignKey(default=0, to='team.Arena'),
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together=set([('date', 'home'), ('date', 'guest')]),
        ),
        migrations.AlterUniqueTogether(
            name='goaltenderstats',
            unique_together=set([('player', 'season')]),
        ),
        migrations.AlterUniqueTogether(
            name='fieldplayerstats',
            unique_together=set([('player', 'season')]),
        ),
    ]
