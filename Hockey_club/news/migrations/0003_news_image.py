# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.URLField(default=0),
        ),
    ]
