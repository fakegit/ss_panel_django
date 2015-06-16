from django.db import models
import datetime,time

# Create your models here.

class Admin_user(models.Model):
    auid = models.CharField(unique=True,max_length=64)
    username = models.CharField(unique=True,max_length=255)
    loginpwd = models.CharField(max_length=255)
    status = models.IntegerField()
    createtime = models.DateTimeField(auto_now_add=True)
    
