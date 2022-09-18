from unicodedata import category
from django.db import models

class time_table(models.Model):
    stt = models.AutoField(primary_key=True)
    hp = models.CharField(max_length=255,null=True,blank=True)
    si_so = models.IntegerField()
    buoi = models.CharField(max_length=10,null=True,blank=True)
    thu = models.IntegerField()
    giang_duong = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        self.hp

class users(models.Model):
    stt = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=30,null=True,blank=True)
    category = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        self.username

