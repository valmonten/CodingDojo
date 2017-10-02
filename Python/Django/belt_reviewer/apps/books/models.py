# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..logreg.models import *

# Create your models here.
class Books(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    
