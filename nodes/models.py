from django.db import models

# Create your models here.

class Nodes(models.Model):
    nodename = models.CharField(unique=True,max_length=255)
    nodetype = models.CharField(unique=True,max_length=20)
    nodeserver = models.CharField(max_length=255)
    nodeenmethod = models.CharField(max_length=20)
    nodedescr = models.CharField(max_length=512)
    nodestatus = models.CharField(max_length=20)
    nodeorder = models.IntegerField()
    
   

