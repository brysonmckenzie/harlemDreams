# Generated by Django 2.2.5 on 2019-10-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(),
        ),
    ]
