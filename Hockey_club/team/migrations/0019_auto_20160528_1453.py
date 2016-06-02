# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-28 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0018_auto_20160527_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_time', models.TimeField(default=b'00:00')),
                ('text', models.TextField()),
                ('online', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='team.Online')),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='online',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
