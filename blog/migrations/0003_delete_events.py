# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_events'),
    ]

    operations = [
        migrations.DeleteModel(
            name='events',
        ),
    ]
