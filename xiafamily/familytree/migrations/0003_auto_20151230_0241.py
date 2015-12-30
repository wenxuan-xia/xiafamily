# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familytree', '0002_auto_20151230_0236'),
    ]

    operations = [
        migrations.DeleteModel(
            name='memberDetail',
        ),
        migrations.AddField(
            model_name='familymember',
            name='careers',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='familymember',
            name='education',
            field=models.TextField(null=True),
        ),
    ]
