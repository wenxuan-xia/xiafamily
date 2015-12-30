# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familytree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='memberDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('familyMemberId', models.IntegerField()),
                ('education', models.TextField()),
                ('careers', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='familymember',
            name='spouse_id',
            field=models.IntegerField(default=0),
        ),
    ]
