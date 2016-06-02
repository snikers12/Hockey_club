# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20160403_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='arena',
            field=models.ForeignKey(to='team.Arena'),
        ),
    ]
