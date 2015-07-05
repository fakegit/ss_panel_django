# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150627_0817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='userpwd',
            new_name='encrptuserpwd',
        ),
        migrations.AddField(
            model_name='users',
            name='transfer_enable',
            field=models.BigIntegerField(default=20000000),
        ),
    ]
