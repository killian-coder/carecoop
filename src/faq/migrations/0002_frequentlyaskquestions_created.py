# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-01 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frequentlyaskquestions',
            name='created',
            field=models.TextField(blank=True, null=True, verbose_name='Created'),
        ),
    ]
