# -*- coding:utf8 -*-

from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(unique=True,max_length=255)
    email = models.CharField(unique=True,max_length=255)
    encrptuserpwd = models.CharField(max_length=255)
    sspwd = models.CharField(max_length=20)
    register_ts = models.IntegerField()
    last_online_ts = models.IntegerField()
    up_transfer = models.BigIntegerField()  #用户上传流量
    down_transfer = models.BigIntegerField()  #用户下载流量
    transfer_enable = models.BigIntegerField(default=20000000)  #用户可用流量
    port = models.IntegerField()
    switch = models.IntegerField() 
    enable = models.BooleanField(default=True)  #用户可用
    usertype = models.IntegerField()  #用户套餐
