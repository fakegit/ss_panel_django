#-*- coding:utf8 -*-
from django import forms
from captcha.fields import CaptchaField
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=30,help_text='100 characters max.')
    email =  forms.EmailField(widget=forms.EmailInput,label='邮箱',max_length=30)
    userpwd = forms.CharField(widget=forms.PasswordInput,label='密码',max_length=150)
    reuserpwd = forms.CharField(widget=forms.PasswordInput,label='确认密码',max_length=150)
    captcha = CaptchaField(label='验证码',)

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=30,help_text='100 characters max.')
    userpwd = forms.CharField(widget=forms.PasswordInput,label='密码',max_length=50)