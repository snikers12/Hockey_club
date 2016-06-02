# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-01 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('news', '0005_remove_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
            preserve_default=False,
        ),
    ]