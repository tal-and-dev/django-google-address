# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 20:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('google_address', '0005_auto_20170418_2304'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GoogleRegion',
        ),
    ]