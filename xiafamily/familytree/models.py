# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class familyMember(models.Model):
    """
        Family member basic information.
    """
    name = models.CharField(null=False, max_length="16")
    generation = models.IntegerField(null=False)

    belongs_to = models.CharField(null=False, max_length="16")
    oldsystem_mark = models.CharField(null=False, max_length="32")
    oldsystem_belongs_to = models.CharField(null=False, max_length="32")

    gender = models.CharField(default="男", max_length="4")
    married = models.BooleanField(default=False)
    parent_id = models.IntegerField(default=0)
    spouse_name = models.CharField(max_length="16", default="")

    education = models.TextField(null=True)
    careers = models.TextField(null=True)
