# -*- coding:utf8 -*-
from __future__ import division
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from . import services
from .forms import RegisterForm,LoginForm,UpdateLoginForm,UpdateSSPwdForm
from users.models import Users
from nodes.models import Nodes
from utils.timeutils import TimeUtils
from utils.strutils import StrUtils
from utils.encrptyutils import EncrptyUtils
from django.db.models import Max
from django.core.mail import send_mail
from json import *
import threading


def login(request):
    form = LoginForm()
    request.session.set_test_cookie()
    return render_to_response('login.html',{'form':form},context_instance = RequestContext(request))

@csrf_exempt
def loginForm(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpwd = form.cleaned_data['userpwd']
            user_data = None
            try:
                user_data = Users.objects.get(username=username)
            except Exception,e:
                return render_to_response('login.html',{'form':form,'errormsg':'您输入的账号有误'})

            if not user_data.actived:
                return render_to_response('login.html',{'form':form,'errormsg':'您输入的账号未激活，请登陆您的注册邮箱'+str(user_data.email)+'进行激活','errorlink':'#','reactiveemail':str(user_data.email)})

            encrptuserpwd = EncrptyUtils.getMd5(userpwd+str(user_data.register_ts))
            if user_data.encrptuserpwd == encrptuserpwd:
                trans_data = user_data.to_dict()
                trans_data['transfer_enable'] =  trans_data['transfer_enable']/1000/1000/1024
                trans_data['transfer_used'] = (trans_data['up_transfer'] + trans_data['down_transfer'])/1000/1000/1024
                trans_data['transfer_last'] = trans_data['transfer_enable']-trans_data['transfer_used']
                trans_data['last_online_ts'] = TimeUtils.getDatetimeFromTS(trans_data['last_online_ts'])
                trans_data['transfer_used_scale'] = trans_data['transfer_used']/trans_data['transfer_enable']*100
                request.session['useruuid'] = trans_data['useruuid']

                return render_to_response('users/users_front.html',trans_data) 
            else:
                return render_to_response('login.html',{'form':form,'errormsg':'您输入的密码有误，请重新输入'})
    else:
        if 'useruuid' in request.session and request.session['useruuid'] is not None:
            user_data = Users.objects.get(useruuid=request.session['useruuid'])
            trans_data = user_data.to_dict()
            trans_data['transfer_enable'] =  trans_data['transfer_enable']/1000/1000/1024
            trans_data['transfer_used'] = (trans_data['up_transfer'] + trans_data['down_transfer'])/1000/1000/1024
            trans_data['transfer_last'] = trans_data['transfer_enable']-trans_data['transfer_used']
            trans_data['last_online_ts'] = TimeUtils.getDatetimeFromTS(trans_data['last_online_ts'])

            request.session['useruuid'] = trans_data['useruuid']   
            return render_to_response('users/users_front.html',trans_data) 
        else:            

            form = LoginForm()
            return render_to_response('login.html',{'form':form},context_instance = RequestContext(request))
    

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

            register_ts = TimeUtils.getTimeStamp()

            user_data = Users(
                useruuid = StrUtils.getUUUID(username+str(register_ts)),
                username = username,
                email = email,
                encrptuserpwd = EncrptyUtils.getMd5(userpwd+str(register_ts)),
                sspwd = StrUtils.getRandomStr(6),
                register_ts = register_ts,
                last_online_ts = register_ts,
                up_transfer = 0,
                down_transfer = 0,
                port = int(Users.objects.aggregate(Max('port'))['port__max'] or 49999)+StrUtils.getRandomNum(1,3),
                switch = 1,
                enable = 1,
                usertype = 0,
                actived=0,
            )
            user_data.save()
            #t1 = threading.Thread(target=send_mail,args=('ss active ', 'http://127.0.0.1:8000/ please click it and active your account', 'ducg@foxmail.com',[email], fail_silently=False))
            #t1.start()
            send_mail('ss active ', 'http://127.0.0.1:8000/ please click it and active your account', 'ducg@foxmail.com',[email], fail_silently=False)
            return render_to_response('users/register_success.html',{'username':username})
        else:
            return render_to_response('register.html',{'form':form})
    else:
        form = RegisterForm()
        return render_to_response(request, 'register.html', {'form': form})

def logout(request):
    form = LoginForm()
    try:
        del request.session['useruuid']
    except KeyError:
        pass
    return render_to_response('login.html',{'form':form},context_instance = RequestContext(request))

def updateUserInfo(request):
    if 'useruuid' in request.session and request.session['useruuid'] is not None:
        user_data = Users.objects.get(useruuid=str(request.session['useruuid']))
        trans_data = user_data.to_dict()
        trans_data['updateLoginForm'] = UpdateLoginForm()
        trans_data['updateSSPwdForm'] = UpdateSSPwdForm()
        return render_to_response('users/users_front_update.html',trans_data)
    else:
        form = LoginForm()
        return render_to_response('login.html',{'form':form}, context_instance = RequestContext(request))


@csrf_exempt
def updateUserInfoForm(request):
    if 'useruuid' in request.session:
        updateLoginForm = UpdateLoginForm(request.POST)
        if updateLoginForm.is_valid():
            oldpwd = updateLoginForm.cleaned_data['oldpwd']
            newpwd = updateLoginForm.cleaned_data['newpwd']
            renewpwd = updateLoginForm.cleaned_data['renewpwd']
            user_data = Users.objects.get(useruuid=str(request.session['useruuid']))

            trans_data = user_data.to_dict()
            trans_data['transfer_enable'] =  trans_data['transfer_enable']/1000/1000/1024
            trans_data['transfer_used'] = (trans_data['up_transfer'] + trans_data['down_transfer'])/1000/1000/1024
            trans_data['transfer_last'] = trans_data['transfer_enable']-trans_data['transfer_used']
            trans_data['last_online_ts'] = TimeUtils.getDatetimeFromTS(trans_data['last_online_ts'])
            trans_data['updateSSPwdForm'] = UpdateSSPwdForm()
            trans_data['updateLoginForm'] = UpdateLoginForm()
            encrptuserpwd = EncrptyUtils.getMd5(oldpwd+str(user_data.register_ts))
            if encrptuserpwd == user_data.encrptuserpwd: 
                if newpwd==renewpwd:
                    user_data.encrptuserpwd = EncrptyUtils.getMd5(newpwd+str(user_data.register_ts))
                    user_data.save()
                    trans_data['scsmsg']='更新密码成功'
                else:
                    trans_data['errmsg']='两次输入的密码不一致'
                return render_to_response('users/users_front_update.html',trans_data)
            else:
                trans_data['errmsg']='原始密码输入错误,密码未修改成功'
                return render_to_response('users/users_front_update.html',trans_data)
    else:
        form = LoginForm()
        return render_to_response('login.html',{'form':form},context_instance = RequestContext(request))

@csrf_exempt
def updateSSPwdForm(request):
    if 'useruuid' in request.session:
        updateSSPwdForm = UpdateSSPwdForm(request.POST)
        if updateSSPwdForm.is_valid():
            sspwd = updateSSPwdForm.cleaned_data['sspwd']
            resspwd = updateSSPwdForm.cleaned_data['resspwd']

            user_data = Users.objects.get(useruuid=str(request.session['useruuid']))

            trans_data = user_data.to_dict()
            trans_data['transfer_enable'] =  trans_data['transfer_enable']/1000/1000/1024
            trans_data['transfer_used'] = (trans_data['up_transfer'] + trans_data['down_transfer'])/1000/1000/1024
            trans_data['transfer_last'] = trans_data['transfer_enable']-trans_data['transfer_used']
            trans_data['last_online_ts'] = TimeUtils.getDatetimeFromTS(trans_data['last_online_ts'])
            trans_data['updateSSPwdForm'] = UpdateSSPwdForm()
            trans_data['updateLoginForm'] = UpdateLoginForm()
            
            if sspwd==resspwd:
                user_data.sspwd = sspwd
                user_data.save()
                trans_data['scsmsg']='更新密码成功'
            else:
                trans_data['errmsg']='两次输入的密码不一致'
            return render_to_response('users/users_front_update.html',trans_data)
    else:
        form = LoginForm()
        return render_to_response('login.html',{'form':form},context_instance = RequestContext(request))

def userCenter(request):
    if 'useruuid' in request.session:
        user_data = Users.objects.get(useruuid=str(request.session['useruuid']))
        trans_data = user_data.to_dict()
        trans_data['transfer_enable'] =  trans_data['transfer_enable']/1000/1000/1024
        trans_data['transfer_used'] = (trans_data['up_transfer'] + trans_data['down_transfer'])/1000/1000/1024
        trans_data['transfer_last'] = trans_data['transfer_enable']-trans_data['transfer_used']
        trans_data['last_online_ts'] = TimeUtils.getDatetimeFromTS(trans_data['last_online_ts'])
        return render_to_response('users/users_front.html',trans_data) 

    else:
        form = LoginForm()
        return render_to_response('login.html',{'form':form},context_instance = RequestContext(request))

def nodeList(request):
    if 'useruuid' in request.session:
        user_data = Users.objects.get(useruuid=str(request.session['useruuid']))
        trans_data = user_data.to_dict()
        nodes_data = Nodes.objects.all()[0]
        trans_data['nodename'] = nodes_data.nodename
        return render_to_response('users/users_nodes.html',trans_data)
    else:
        form = LoginForm()
        return render_to_response('login.html',{'form':form},context_instance = RequestContext(request))

@csrf_exempt
def reSendActiveEmail(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        d = {}
        d['result'] = 0

        try:
            user_data = Users.objects.get(username=username,email=useremail)
        except Exception,e:
            d['msg'] = '激活邮件未发送成功，您输入的用户名和邮箱不匹配'
            json_data = JSONEncoder().encode(d)
            return HttpResponse(json_data,content_type="application/json")
            
        send_mail('ss active ', 'http://127.0.0.1:8000/ please click it and active your account', 'ducg@foxmail.com',[email], fail_silently=False)
        d['result'] = 1
        d['msg'] = '激活邮件发送，请登陆邮箱进行激活'
        json_data = JSONEncoder().encode(d)
        return HttpResponse(json_data,content_type='application/json')

    else:
        return HttpResponse('hehe')
