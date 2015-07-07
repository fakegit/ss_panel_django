# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150629_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='useruuid',
            field=models.CharField(default=datetime.datetime(2015, 7, 5, 12, 47, 39, 611509, tzinfo=utc), unique=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='transfer_enable',
            field=models.BigIntegerField(default=2048000000),
        ),
    ]
