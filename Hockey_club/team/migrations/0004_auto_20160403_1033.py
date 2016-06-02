# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20160403_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arena',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
