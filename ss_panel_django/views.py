from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.core.mail import send_mail

def index(request):
    
    return render_to_response('index.html')



