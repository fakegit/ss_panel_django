# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150705_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='useruuid',
            field=models.CharField(max_length=255),
        ),
    ]
