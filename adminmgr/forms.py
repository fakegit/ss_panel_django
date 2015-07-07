#-*- coding:utf8 -*-
from django import forms
from captcha.fields import CaptchaField
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json



class AdminLoginForm(forms.Form):
    adminusername = forms.CharField(label='用户名',max_length=30)
    adminuserpwd = forms.CharField(widget=forms.PasswordInput,label='密码',max_length=50)
