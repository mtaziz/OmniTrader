# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0013_trade_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
    ]
