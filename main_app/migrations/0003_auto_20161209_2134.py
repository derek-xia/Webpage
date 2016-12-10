# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20161126_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='img_url',
        ),
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='main_app'),
        ),
    ]