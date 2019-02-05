# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CAR(models.Model):
    C_Name = models.CharField(max_length=125)
    C_Model = models.CharField(max_length=125)
    C_Loanch = models.DateField()
    C_Price = models.CharField(max_length=125)

class BOOK(models.Model):
    B_Title = models.CharField(max_length=125)
    B_Author = models.CharField(max_length=125)
    B_pages = models.CharField(max_length=125)
    B_Price = models.CharField(max_length=125)

class FOOD(models.Model):
    F_Name = models.CharField(max_length=125)
    F_Price = models.CharField(max_length=125)