# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familyMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'16')),
                ('generation', models.IntegerField()),
                ('belongs_to', models.CharField(max_length=b'16')),
                ('gender', models.CharField(default=b'\xe7\x94\xb7', max_length=b'4')),
                ('married', models.BooleanField(default=False)),
                ('parent_id', models.IntegerField(default=0)),
            ],
        ),
    ]
