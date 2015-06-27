# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_register_ts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='type',
            new_name='usertype',
        ),
    ]
