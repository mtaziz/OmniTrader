# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0014_trade_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('filename', models.CharField(max_length=127)),
                ('date', models.DateField()),
                ('account', models.ForeignKey(to='stocks.Account', related_name='recordfiles')),
            ],
        ),
    ]
