# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('email', models.CharField(unique=True, max_length=255)),
                ('userpwd', models.CharField(max_length=255)),
                ('sspwd', models.CharField(max_length=20)),
                ('last_online_ts', models.IntegerField()),
                ('up_transfer', models.BigIntegerField()),
                ('down_transfer', models.BigIntegerField()),
                ('port', models.IntegerField()),
                ('switch', models.IntegerField()),
                ('enable', models.BooleanField(default=True)),
                ('type', models.IntegerField()),
            ],
        ),
    ]
