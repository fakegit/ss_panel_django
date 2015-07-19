# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150705_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='actived',
            field=models.BooleanField(default=False),
        ),
    ]
