# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('stocks', '0016_traderecord_trader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocktagrel',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='stocktagrel',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='stocks',
        ),
        migrations.AddField(
            model_name='stock',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='StockTagRel',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
