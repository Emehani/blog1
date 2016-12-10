
from __future__ import unicode_literals
from django.db import models




class B1(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=520)