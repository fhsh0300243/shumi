# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0002_remove_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DishTitle', models.CharField(max_length=200)),
                ('DishContent', models.TextField(blank=True)),
                ('DishPhoto', models.URLField(blank=True)),
                ('DishCreated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
