# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardsApp', '0003_auto_20170217_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='card',
            name='power',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='toughness',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
