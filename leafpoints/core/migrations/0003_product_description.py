# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150411_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.URLField(max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
