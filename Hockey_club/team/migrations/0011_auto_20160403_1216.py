# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_auto_20160403_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamstuff',
            name='position',
            field=models.CharField(max_length=50, choices=[(b'Coach', b'C'), (b'President', b'P'), (b'Head coach', b'HC'), (b'General manager', b'GM'), (b'Doctor', b'D'), (b"Goaltender's coach", b'GC'), (b'Masseur', b'M')]),
        ),
    ]
