# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-07-12 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helvetic', '0002_auto_20200712_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='synced_to_hk',
            field=models.BooleanField(default=False),
        ),
    ]
