# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminmgr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_user',
            name='loginpwd',
            field=models.CharField(max_length=255),
        ),
    ]
