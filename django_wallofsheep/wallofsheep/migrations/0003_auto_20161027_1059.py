# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallofsheep', '0002_auto_20161027_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sheeps_table',
            old_name='option',
            new_name='method',
        ),
    ]
