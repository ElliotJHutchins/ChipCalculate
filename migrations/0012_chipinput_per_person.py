# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChipCalculate', '0011_chipcalculate_number_of_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='chipinput',
            name='per_person',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
