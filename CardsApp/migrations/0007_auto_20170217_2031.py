# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardsApp', '0006_auto_20170217_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='artist',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='cardid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='cmc',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='imageName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='layout',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='multiverseid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='rarity',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='typeString',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
