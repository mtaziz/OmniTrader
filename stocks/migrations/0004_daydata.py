# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20150418_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('open', models.DecimalField(max_digits=6, decimal_places=2)),
                ('close', models.DecimalField(max_digits=6, decimal_places=2)),
                ('high', models.DecimalField(max_digits=6, decimal_places=2)),
                ('low', models.DecimalField(max_digits=6, decimal_places=2)),
                ('adj_open', models.DecimalField(max_digits=6, decimal_places=2)),
                ('adj_close', models.DecimalField(max_digits=6, decimal_places=2)),
                ('adj_high', models.DecimalField(max_digits=6, decimal_places=2)),
                ('adj_low', models.DecimalField(max_digits=6, decimal_places=2)),
                ('volume', models.IntegerField()),
                ('stock', models.ForeignKey(to='stocks.Stock')),
            ],
        ),
    ]
