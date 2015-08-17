# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_auto_20150816_1027'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='daydata',
            index_together=set([('stock', 'date')]),
        ),
    ]
