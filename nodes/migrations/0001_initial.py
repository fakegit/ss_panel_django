# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nodename', models.CharField(unique=True, max_length=255)),
                ('nodetype', models.CharField(unique=True, max_length=20)),
                ('nodeserver', models.CharField(max_length=255)),
                ('nodeenmethod', models.CharField(max_length=20)),
                ('nodedescr', models.CharField(max_length=512)),
                ('nodestatus', models.CharField(max_length=20)),
                ('nodeorder', models.IntegerField()),
            ],
        ),
    ]
