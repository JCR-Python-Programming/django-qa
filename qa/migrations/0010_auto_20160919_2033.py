# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0009_auto_20160919_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-answer', '-pub_date']},
        ),
    ]