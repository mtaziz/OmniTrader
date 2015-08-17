# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0008_auto_20150817_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(db_index=True, max_length=10),
        ),
    ]
