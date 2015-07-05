from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from . import services
from .forms import RegisterForm,LoginForm
from users.models import Users
from utils.timeutils import TimeUtils
from utils.strutils import StrUtils
from utils.encrptyutils import EncrptyUtils
from django.db.models import Max
# Create your views here.


def login(request):
    form = LoginForm()
    return render_to_response('login.html',{'form':form},context_instance = RequestContext(request))

@csrf_exempt
def loginForm(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpwd = form.cleaned_data['userpwd']
            user_data = Users.objects.get(username=username)
            encrptuserpwd = EncrptyUtils.getMd5(userpwd+str(user_data.register_ts))
            print encrptuserpwd
            print user_data.encrptuserpwd
            if user_data.encrptuserpwd == encrptuserpwd:
                return render_to_response('users/users_front.html',{'username':username}) 

            return render_to_response('users/users_front.html',{'username':user_data.encrptuserpwd})

    return render_to_response('users/users_front.html')


def register(request):
    form = RegisterForm()

    return render_to_response('register.html',{'form':form}, context_instance = RequestContext(request))

@csrf_exempt
def registerForm(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpwd = form.cleaned_data['userpwd']
            email = form.cleaned_data['email']
            reuserpwd = form.cleaned_data['reuserpwd']

            #rst,errmsg = services.UsersService.regParamCheck(username,email,userpwd,reuserpwd)
            #if not rst:
            #    return render_to_response('register.html',{'errmsg':errmsg})

            register_ts = TimeUtils.getTimeStamp()

            user_data = Users(
                username = username,
                email = email,
                encrptuserpwd = EncrptyUtils.getMd5(userpwd+str(register_ts)),
                sspwd = StrUtils.getRandomStr(6),
                register_ts = register_ts,
                last_online_ts = register_ts,
                up_transfer = 0,
                down_transfer = 0,
                port = int(Users.objects.aggregate(Max('port'))['port__max'])+1,
                switch = 1,
                enable = 1,
                usertype = 0,
            )
            user_data.save()

            return render_to_response('users/register_success.html',{'username':username})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



