# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 03:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20180709_0548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='like',
        ),
    ]
