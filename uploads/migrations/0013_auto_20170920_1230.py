# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-20 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0012_merge_20170920_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='user',
        ),
        migrations.AlterField(
            model_name='upload',
            name='docFile',
            field=models.FileField(blank=True, default=None, null=True, upload_to=b''),
        ),
    ]
