# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-11 00:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0011_auto_20200511_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitelink',
            old_name='email_CONTACT',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='sitelink',
            old_name='phone_number_CONTACT',
            new_name='contact_page_phone',
        ),
        migrations.RenameField(
            model_name='sitelink',
            old_name='phone_number_HOME',
            new_name='homepage_phone',
        ),
    ]