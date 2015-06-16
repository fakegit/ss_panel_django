# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auid', models.CharField(unique=True, max_length=64)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('loginpwd', models.CharField(unique=True, max_length=255)),
                ('status', models.IntegerField()),
                ('createtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
