# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_auto_20160403_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_time',
            field=models.DurationField(),
        ),
    ]
