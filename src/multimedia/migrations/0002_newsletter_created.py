# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-01 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='created',
            field=models.TextField(blank=True, null=True, verbose_name='Created'),
        ),
    ]