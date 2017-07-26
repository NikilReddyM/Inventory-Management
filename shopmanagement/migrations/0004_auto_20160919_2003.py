# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopmanagement', '0003_item_min_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='min_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
