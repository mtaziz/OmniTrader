# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_auto_20150815_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daydata',
            name='adj_close',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='adj_high',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='adj_low',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='adj_open',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='close',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='high',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='low',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='open',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6),
        ),
    ]
