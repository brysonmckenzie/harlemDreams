# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-11 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0010_auto_20200511_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitelink',
            name='email_CONTACT',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='sitelink',
            name='phone_number_CONTACT',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sitelink',
            name='phone_number_HOME',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
