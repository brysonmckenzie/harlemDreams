# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-10 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0008_auto_20200510_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitelink',
            name='facebook',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='sitelink',
            name='instagram',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='sitelink',
            name='twitter',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]