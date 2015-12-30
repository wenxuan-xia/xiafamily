# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familytree', '0003_auto_20151230_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymember',
            name='spouse_id',
        ),
        migrations.AddField(
            model_name='familymember',
            name='spouse_name',
            field=models.CharField(default=b'', max_length=b'16'),
        ),
    ]
