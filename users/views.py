from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.views.decorators.csrf import csrf_exempt
from . import services
from .forms import RegisterForm
from users.models import Users
from utils.timeutils import TimeUtils
from utils.strutils import StrUtils
from utils.encrptyutils import EncrptyUtils
from django.db.models import Max
# Create your views here.


def login(request):
    return render_to_response('login.html')



def register(request):
    form = RegisterForm()

    return render_to_response('register.html',{'form':form})

@csrf_exempt
def registerForm(request):
    if request.method =='GET':
        raise  Http404
    username = request.POST.get('username')
    email = request.POST.get('email')
    userpwd = request.POST.get('userpwd')
    reuserpwd = request.POST.get('reuserpwd')

    rst,errmsg = services.UsersService.regParamCheck(username,email,userpwd,reuserpwd)
    if not rst:
        return render_to_response('register.html',{'errmsg':errmsg})

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

@csrf_exempt
def registerForm1(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpwd = form.cleaned_data['userpwd']
            email = form.cleaned_data['email']
            reuserpwd = form.cleaned_data['reuserpwd']

            return render_to_response('users/register_success.html',{'username':username})
        else:
            raise Http404
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@csrf_exempt
def loginForm(request):
    if request.method=='GET':
        raise  Http404
    username = request.POST.get('username')
    userpwd = request.POST.get('userpwd')
    return render_to_response('users/users_front.html')
