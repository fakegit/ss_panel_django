# -*- coding:utf8 -*-
from django.core.mail import send_mail
from django.conf import settings  
settings.configure()

def sendmail():
    #print 'fsdfs'
    #send_mail('Subject here', 'Here is the message.', 'ducg@foxmail.com',['strengthening@aliyun.com'], fail_silently=False)

if __name__== '__main__':
    sendmail()