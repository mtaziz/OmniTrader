# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_auto_20150817_2152'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='daydata',
            unique_together=set([('stock', 'date')]),
        ),
    ]
