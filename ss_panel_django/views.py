from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.core.mail import send_mail

def index(request):
    send_mail('Subject here', 'Here is the message.', 'strengthen2010@gmail.com',['strengthening@aliyun.com'], fail_silently=False)
    return render_to_response('index.html')



