# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150705_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='useruuid',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
