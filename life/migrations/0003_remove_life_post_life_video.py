# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-09 07:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_life_post_life_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='life_post',
            name='Life_video',
        ),
    ]
