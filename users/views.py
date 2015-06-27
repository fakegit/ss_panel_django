from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.views.decorators.csrf import csrf_exempt
from . import services
# Create your views here.


def login(request):
    return render_to_response('login.html')



def register(request):


    return render_to_response('register.html')

@csrf_exempt
def registerForm(request):
    if request.method=='GET':
        raise  Http404
    username = request.POST.get('username')
    email = request.POST.get('email')
    userpwd = request.POST.get('userpwd')
    reuserpwd = request.POST.get('reuserpwd')

    rst,errmsg = services.UsersService.regParamCheck(username,email,userpwd,reuserpwd)
    if not rst:
        return render_to_response('register.html',{'errmsg':errmsg})

    
    return render_to_response('users/register_success.html',{'username':username})

