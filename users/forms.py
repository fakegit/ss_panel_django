#-*- coding:utf8 -*-
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=30,help_text='100 characters max.')
    email =  forms.EmailField(label='邮箱',max_length=30)
    userpwd = forms.CharField(label='密码',max_length=50)
    reuserpwd = forms.CharField(label='确认密码',max_length=50)