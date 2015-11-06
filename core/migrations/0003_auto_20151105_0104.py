# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151105_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
