# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-04-04 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0006_auto_20200404_0656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roster',
            old_name='player_bio',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='roster',
            old_name='player_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='roster',
            old_name='player_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='roster',
            old_name='player_quote',
            new_name='quote',
        ),
    ]