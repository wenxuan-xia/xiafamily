# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class familyMember(models.Model):
    """
        Family member basic information.
    """
    name = models.CharField(null=True, max_length=16)
    house = models.CharField(null=True, max_length=32, default="未知")
    generation = models.CharField(null=True, max_length=16)

    belongs_to = models.CharField(null=True, max_length=16)
    oldsystem_id = models.IntegerField(default=0)

    gender = models.CharField(default="男", max_length=16)
    married = models.BooleanField(default=False, null=False)
    # parent_id = models.IntegerField(default=0)
    spouse_name = models.CharField(max_length=16, default="-", null=False)

    location = models.TextField(null=False, default="0")
    education = models.TextField(null=False, default="0")
    careers = models.TextField(null=False, default="0")
    links = models.TextField(null=False, default="0")
