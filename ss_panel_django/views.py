from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response 

def index(request):
    return render_to_response('index.html')

def introduction(request):
    return render_to_response('introduction.html')

