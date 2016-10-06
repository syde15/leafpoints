# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterSavings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('water_saved', models.DecimalField(max_digits=8, decimal_places=2)),
                ('daily_savings', models.BooleanField()),
                ('product_life', models.IntegerField()),
                ('product', models.ForeignKey(to='core.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
