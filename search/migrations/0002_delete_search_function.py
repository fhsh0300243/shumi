# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Search_function',
        ),
    ]