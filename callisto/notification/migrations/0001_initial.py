# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-30 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewEmailNotification',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=77)),
                ('body', models.TextField()),
            ],
        ),
    ]
