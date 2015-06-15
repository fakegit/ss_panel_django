from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(unique=True,max_length=255)
    email = models.CharField(unique=True,max_length=255)
    userpwd = models.CharField(max_length=255)
    sspwd = models.CharField(max_length=20)
    last_online_ts = models.IntegerField()
    up_transfer = models.BigIntegerField()
    down_transfer = models.BigIntegerField()
    port = models.IntegerField()
    switch = models.IntegerField()
    enable = models.BooleanField(default=True)
    type = models.IntegerField()
