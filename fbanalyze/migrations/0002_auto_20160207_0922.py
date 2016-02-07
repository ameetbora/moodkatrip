# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbanalyze', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='places',
            options={'verbose_name_plural': 'Places'},
        ),
        migrations.AlterField(
            model_name='places',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='places',
            name='type',
            field=models.CharField(max_length=150),
        ),
    ]
