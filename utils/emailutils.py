# -*- coding:utf8 -*-
from django.core.mail import send_mail
from ss_panel_django import settings

def sendmail():
    send_mail('Subject here', 'Here is the message.', 'strengthen2010@gmail.com',
    ['ducg@foxmail.com'], fail_silently=False)

if __name__== '__main__':
    sendmail()