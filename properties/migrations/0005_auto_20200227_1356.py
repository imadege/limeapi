# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-02-27 13:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20200227_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='property',
            new_name='property_booking',
        ),
    ]
