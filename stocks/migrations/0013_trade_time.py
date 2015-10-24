# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0012_auto_20151021_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='time',
            field=models.DateField(null=True, blank=True),
        ),
    ]
