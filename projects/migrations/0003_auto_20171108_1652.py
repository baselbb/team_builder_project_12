# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20171106_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='skill',
        ),
        migrations.AddField(
            model_name='position',
            name='skills',
            field=models.ManyToManyField(default='', null=True, to='projects.Skill'),
        ),
    ]
