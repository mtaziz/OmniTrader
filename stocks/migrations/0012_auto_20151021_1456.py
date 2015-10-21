# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0011_trade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.AddField(
            model_name='trade',
            name='account',
            field=models.ForeignKey(null=True, to='stocks.Account', blank=True, related_name='trades'),
        ),
        migrations.AddField(
            model_name='trade',
            name='trader',
            field=models.ForeignKey(null=True, to='stocks.Trader', blank=True, related_name='trades'),
        ),
    ]
