# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_stock_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='active',
            new_name='rzrq',
        ),
    ]
