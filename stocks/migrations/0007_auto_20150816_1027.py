# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_auto_20150815_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daydata',
            name='stock',
            field=models.ForeignKey(related_name='dayHist', to='stocks.Stock'),
        ),
    ]
