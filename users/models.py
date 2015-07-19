# -*- coding:utf8 -*-

from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.


class Users(models.Model):
    useruuid = models.CharField(unique=True,max_length=255) #用户uuid
    username = models.CharField(unique=True,max_length=255)
    email = models.CharField(unique=True,max_length=255)
    encrptuserpwd = models.CharField(max_length=255)
    sspwd = models.CharField(max_length=20)
    register_ts = models.IntegerField()
    last_online_ts = models.IntegerField()
    up_transfer = models.BigIntegerField()  #用户上传流量
    down_transfer = models.BigIntegerField()  #用户下载流量
    transfer_enable = models.BigIntegerField(default=2048000000)  #用户可用流量
    port = models.IntegerField()
    switch = models.IntegerField() 
    actived = models.BooleanField(default=False)#用户是否邮箱激活
    enable = models.BooleanField(default=True)  #用户可用
    usertype = models.IntegerField()  #用户套餐

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data
