# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-02 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0004_auto_20170902_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ['-created'], 'verbose_name': 'NEWS LETTER', 'verbose_name_plural': 'NEWS LETTERS'},
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='successstories',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]