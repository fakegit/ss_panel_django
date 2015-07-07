from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.http import HttpResponse
from django.template import RequestContext
from .forms import AdminLoginForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    form = AdminLoginForm()
    return render_to_response('adminmgr/admin_login.html',{'form':form})
    
@csrf_exempt
def adminLoginForm(request):

    return render_to_response('adminmgr/admin_front.html')
