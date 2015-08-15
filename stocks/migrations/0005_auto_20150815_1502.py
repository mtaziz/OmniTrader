# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_daydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daydata',
            name='adj_close',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='adj_high',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='adj_low',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='adj_open',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='close',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='high',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='low',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=6),
        ),
        migrations.AlterField(
            model_name='daydata',
            name='open',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=6),
        ),
    ]
