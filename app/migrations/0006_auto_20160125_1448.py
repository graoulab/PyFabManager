# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160125_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='Utilisateur',
        ),
        migrations.AddField(
            model_name='projet',
            name='Utilisateur',
            field=models.ManyToManyField(to='app.utilisateur'),
        ),
    ]
