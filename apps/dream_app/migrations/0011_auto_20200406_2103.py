# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-04-06 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0010_auto_20200406_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='carousel'),
        ),
    ]