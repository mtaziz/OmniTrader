# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0015_traderecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='traderecord',
            name='trader',
            field=models.ForeignKey(default=1, related_name='recordfiles', to='stocks.Trader'),
            preserve_default=False,
        ),
    ]
