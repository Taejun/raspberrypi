__author__ = 'taejun'

from django.db import models

class Doc(models.Model):
    dsubject=models.CharField(max_length=255, db_index=True)
    contents=models.TextField(blank=True)
    writer=models.CharField(max_length=40 ,blank=True)
    flag=models.CharField(max_length=20,blank=True)
    reg_date=models.DateTimeField('date written')
